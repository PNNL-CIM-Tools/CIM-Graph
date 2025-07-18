<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:a="http://langdale.com.au/2005/Message#"
    xmlns:sawsdl="http://www.w3.org/ns/sawsdl"
    xmlns:fn="http://www.w3.org/2005/xpath-functions"
    xmlns:local="urn:local-functions"
    xmlns="http://langdale.com.au/2009/Indent"
    exclude-result-prefixes="xs fn local">

    <xsl:output indent="yes" method="xml" encoding="utf-8"/>

    <!-- Parameters with default values -->
    <xsl:param name="version" as="xs:string?" select="()"/>
    <xsl:param name="baseURI" as="xs:string" required="yes"/>
    <xsl:param name="ontologyURI" as="xs:string" required="yes"/>
    <xsl:param name="envelope" as="xs:string" select="'Profile'"/>
    <xsl:param name="package" as="xs:string" select="'au.com.langdale.cimtool.generated'"/>

    <!-- Key for tracing parent-child inheritance -->
    <xsl:key name="classes_by_super" match="a:Root | a:ComplexType" use="a:SuperType/@name"/>

    <!-- Key for finding inverse references by target class -->
    <xsl:key name="inverse_references" match="a:InverseReference | a:InverseInstance" use="substring-after(@inverseBasePropertyClass, '#')"/>

    <xsl:variable name="python_keywords" as="xs:string*" select="(
            'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
            'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
            'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
            'raise', 'return', 'try', 'while', 'with', 'yield'
        )"/>

    <!-- Template for top-level item in schema file -->
    <xsl:template match="a:Catalog">
        <document>
            <!-- Header imports -->
            <xsl:call-template name="generate_imports"/>

            <!-- Documentation -->
            <xsl:call-template name="generate_documentation"/>

            <!-- Generate CIMStereotype enum -->
            <xsl:call-template name="generate_cim_stereotype_enum"/>

            <!-- Constants -->
            <item>BASE_URI = '<xsl:value-of select="$baseURI"/>'</item>
            <item>ONTOLOGY_URI = '<xsl:value-of select="$ontologyURI"/>#'</item>
            <item/>

            <!-- Process classes hierarchically -->
            <xsl:apply-templates select="a:Root[not(a:SuperType)] | a:ComplexType[not(a:SuperType)]" mode="super"/>

            <!-- Process enumerations -->
            <xsl:apply-templates select="a:EnumeratedType" mode="enumeration"/>

            <!-- Process primitives -->
            <xsl:apply-templates select="a:SimpleType" mode="units"/>

            <!-- Process compounds -->
            <xsl:apply-templates select="a:CompoundType" mode="super"/>
        </document>
    </xsl:template>

    <!-- Generate imports section -->
    <xsl:template name="generate_imports">
        <item>from __future__ import annotations</item>
        <item>import logging</item>
        <item>from dataclasses import dataclass, field</item>
        <item>from typing import Optional</item>
        <item>from enum import Enum</item>
        <item>from cimgraph.data_profile.identity import Identity, stereotype</item>
        <item>from cimgraph.data_profile.units import CIMUnit, UnitSymbol, UnitMultiplier</item>
        <item>_log = logging.getLogger(__name__)</item>
    </xsl:template>

    <!-- Generate documentation section -->
    <xsl:template name="generate_documentation">
        <list begin="'''" indent="" end="'''">
            <item>Annotated CIMantic Graphs data profile for <xsl:value-of select="$envelope"/></item>
            <item>Generated by CIMTool http://cimtool.org</item>
        </list>
        <item/>
    </xsl:template>

    <!-- Template for top-level classes with no inheritance -->
    <xsl:template match="a:Root | a:ComplexType | a:CompoundType" mode="super">
        <xsl:call-template name="generate_stereotype"/>

        <xsl:variable name="class_name" select="local:sanitize_name(@name, @name)"/>

        <item>@dataclass(repr=False)</item>
        <item>class <xsl:value-of select="$class_name"/>(Identity):</item>

        <xsl:call-template name="generate_class_docstring"/>

        <!-- Process inverse references first (they come from other classes) -->
        <xsl:apply-templates select="key('inverse_references', @name)" mode="inverse_association"/>

        <!-- Process attributes -->
        <xsl:apply-templates select="a:Simple" mode="simple_attribute"/>
        <xsl:apply-templates select="a:Domain | a:Enumerated" mode="attribute"/>
        <xsl:apply-templates select="a:Instance | a:Reference" mode="association"/>

        <!-- Process child classes -->
        <xsl:apply-templates select="key('classes_by_super', @name)" mode="lower"/>
    </xsl:template>

    <!-- Template for lower level classes -->
    <xsl:template match="a:Root | a:ComplexType" mode="lower">
        <xsl:if test=". is key('classes_by_super', a:SuperType/@name)[1]">
            <xsl:for-each select="key('classes_by_super', a:SuperType/@name)">
                <xsl:call-template name="generate_stereotype"/>

                <item>@dataclass(repr=False)</item>

                <xsl:variable name="class_name" select="local:sanitize_name(@name, @name)"/>
                <item>class <xsl:value-of select="$class_name"/>(<xsl:value-of select="a:SuperType/@name"/>):</item>

                <xsl:call-template name="generate_class_docstring"/>

                <!-- Process inverse references first (they come from other classes) -->
                <xsl:apply-templates select="key('inverse_references', @name)" mode="inverse_association"/>

                <!-- Process attributes -->
                <xsl:apply-templates select="a:Simple" mode="simple_attribute"/>
                <xsl:apply-templates select="a:Domain | a:Enumerated" mode="attribute"/>
                <xsl:apply-templates select="a:Instance | a:Reference" mode="association"/>

                <!-- Process child classes -->
                <xsl:apply-templates select="key('classes_by_super', @name)" mode="lower"/>
            </xsl:for-each>
        </xsl:if>
    </xsl:template>

    <!-- Generate stereotype decorator -->
    <xsl:template name="generate_stereotype">
        <!-- Parse Stereotype -->
        <xsl:for-each select="a:Stereotype">
            <item>@stereotype(CIMStereotype.<xsl:value-of select="local:sanitize_name(@label, @label)"/>)</item>
        </xsl:for-each>
    </xsl:template>

    <!-- Generate class docstring -->
    <xsl:template name="generate_class_docstring">
            <list begin="    '''" indent="    " end="    '''">
                <xsl:for-each select="a:Comment">
                    <wrap width="70">
                        <xsl:value-of select="."/>
                    </wrap>
                </xsl:for-each>
            </list>
            <item/>
    </xsl:template>

    <!-- Generate class docstring -->
    <xsl:template name="generate_attr_docstring">
        <list begin="'''" indent="" end="'''">
            <xsl:for-each select="a:Comment">
                <wrap width="66">
                    <xsl:value-of select="."/>
                </wrap>
            </xsl:for-each>
        </list>
        <item/>
    </xsl:template>

    <!-- Template for processing inverse references -->
    <xsl:template match="a:InverseReference | a:InverseInstance" mode="inverse_association">
        <xsl:variable name="field_name" select="local:sanitize_name(@name, (@type, 'unknown')[1])"/>
        <xsl:variable name="target_type" select="@type"/>
        <xsl:variable name="inverse_property" select="substring-after(@inverseBaseProperty, '#')"/>

        <list begin="" indent="    " end="">
            <xsl:choose>
                <xsl:when test="(@maxOccurs castable as xs:integer and xs:integer(@maxOccurs) le 1) or @maxOccurs = '1' or @maxOccurs = '0'">
                    <item>
                        <xsl:value-of select="$field_name"/>: Optional[<xsl:value-of select="$target_type"/>] = field(
                    </item>
                    <list begin="" indent="    " end="">
                        <item>default=None,</item>
                    </list>
                </xsl:when>
                <xsl:otherwise>
                    <item>
                        <xsl:value-of select="$field_name"/>: list[<xsl:value-of select="$target_type"/>] = field(
                    </item>
                    <list begin="" indent="    " end="">
                        <item>default_factory=list,</item>
                    </list>
                </xsl:otherwise>
            </xsl:choose>

            <list begin="" indent="    " end="">
                <item>metadata={</item>
                <xsl:call-template name="generate_inverse_association_metadata"/>
                <item>})</item>
            </list>

            <xsl:call-template name="generate_attr_docstring"/>
        </list>
    </xsl:template>

    <!-- Template for Domain attributes with datatypes -->
    <xsl:template match="a:Domain | a:Enumerated" mode="attribute">
        <xsl:if test="(@maxOccurs castable as xs:integer and xs:integer(@maxOccurs) le 1) or @maxOccurs = '1' or @maxOccurs = '0'">
            <xsl:variable name="python_type" select="local:get_python_type(@xstype)"/>
            <xsl:variable name="field_name" select="local:sanitize_name(@name, (@type, 'unknown')[1])"/>

            <list begin="" indent="    " end="">
                <item>
                    <xsl:value-of select="$field_name"/>: Optional[
                    <xsl:choose>
                        <xsl:when test="$python_type = 'str'">
                            <xsl:value-of select="(@type, 'str')[1]"/>
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:value-of select="$python_type"/> | <xsl:value-of select="(@type, 'str')[1]"/>
                        </xsl:otherwise>
                    </xsl:choose>
                    ] = field(
                </item>

                <list begin="" indent="    " end="">
                    <item>default=None,</item>
                    <item>metadata={</item>
                    <xsl:call-template name="generate_attribute_metadata"/>
                    <item>})</item>
                </list>

                <xsl:call-template name="generate_attr_docstring"/>
            </list>
        </xsl:if>
    </xsl:template>

    <!-- Template for Simple attributes with primitive datatypes -->
    <xsl:template match="a:Simple" mode="simple_attribute">
        <xsl:if test="(@maxOccurs castable as xs:integer and xs:integer(@maxOccurs) le 1) or @maxOccurs = '1' or @maxOccurs = '0'">
            <xsl:variable name="python_type" select="local:get_python_type(@xstype)"/>
            <xsl:variable name="field_name" select="local:sanitize_name(@name, (@xstype, 'unknown')[1])"/>

            <list begin="" indent="    " end="">
                <item>
                    <xsl:value-of select="$field_name"/>: Optional[<xsl:value-of select="$python_type"/>] = field(
                </item>

                <list begin="" indent="    " end="">
                    <item>default=None,</item>
                    <item>metadata={</item>
                    <xsl:call-template name="generate_attribute_metadata"/>
                    <item>})</item>
                </list>

                <xsl:call-template name="generate_attr_docstring"/>
            </list>
        </xsl:if>
    </xsl:template>

    <!-- Template for associations with other classes -->
    <xsl:template match="a:Instance | a:Reference" mode="association">
        <xsl:variable name="field_name" select="local:sanitize_name(@name, (@type, 'unknown')[1])"/>

        <list begin="" indent="    " end="">
            <xsl:choose>
                <xsl:when test="(@maxOccurs castable as xs:integer and xs:integer(@maxOccurs) le 1) or @maxOccurs = '1' or @maxOccurs = '0'">
                    <item>
                        <xsl:value-of select="$field_name"/>: Optional[<xsl:value-of select="(@type, 'object')[1]"/>] = field(
                    </item>
                    <list begin="" indent="    " end="">
                        <item>default=None,</item>
                    </list>
                </xsl:when>
                <xsl:otherwise>
                    <item>
                        <xsl:value-of select="$field_name"/>: list[<xsl:value-of select="(@type, 'object')[1]"/>] = field(
                    </item>
                    <list begin="" indent="    " end="">
                        <item>default_factory=list,</item>
                    </list>
                </xsl:otherwise>
            </xsl:choose>

            <list begin="" indent="    " end="">
                <item>metadata={</item>
                <xsl:call-template name="generate-association-metadata"/>
                <item>})</item>
            </list>

            <xsl:call-template name="generate_attr_docstring"/>
        </list>
    </xsl:template>

    <!-- Template for enumerations -->
    <xsl:template match="a:EnumeratedType" mode="enumeration">
        <xsl:variable name="enum-name" select="local:sanitize_name(@name, @name)"/>

        <xsl:call-template name="generate_stereotype"/>
        <item>class <xsl:value-of select="$enum-name"/>(Enum):</item>

        <xsl:call-template name="generate_class_docstring"/>

        <xsl:for-each select="a:EnumeratedValue">
            <xsl:variable name="value-name" select="local:sanitize_name(@name, @name)"/>
            <list begin="" indent="    " end="">
                <item><xsl:value-of select="$value-name"/> = '<xsl:value-of select="$value-name"/>'</item>
                <xsl:call-template name="generate_attr_docstring"/>
            </list>
        </xsl:for-each>
    </xsl:template>

    <!-- Template for CIM Units as SimpleType -->
    <xsl:template match="a:SimpleType" mode="units">
        <xsl:call-template name="generate_stereotype"/>
        <item>@dataclass(repr=False)</item>
        <item>class <xsl:value-of select="@name"/>(CIMUnit):</item>

        <xsl:call-template name="generate_class_docstring"/>

        <!-- Process Simple elements -->
        <xsl:for-each select="a:Simple">
            <xsl:variable name="python_type" select="local:get_python_type(@xstype)"/>
            <list begin="" indent="    " end="">
                <item><xsl:value-of select="@name"/>: <xsl:value-of select="$python_type"/> = field(default=None)</item>
            </list>
        </xsl:for-each>

        <!-- Process multiplier fields -->
        <xsl:for-each select="a:Enumerated[@name='multiplier']">
            <xsl:variable name="multiplier-const" select="if (@constant = '' or @constant = 'none') then 'none' else @constant"/>
            <list begin="" indent="    " end="">
                <item><xsl:value-of select="@name"/>: <xsl:value-of select="@type"/> = field(default=<xsl:value-of select="@type"/>.<xsl:value-of select="$multiplier-const"/>)</item>
            </list>
        </xsl:for-each>

        <!-- Process unit fields as properties -->
        <xsl:for-each select="a:Enumerated[@name='unit']">
            <xsl:variable name="unit-const" select="if (@constant = '' or @constant = 'none') then 'none' else @constant"/>
            <list begin="" indent="    " end="">
                <item>@property  # read-only</item>
                <item>def <xsl:value-of select="@name"/>(self):</item>
                <list begin="" indent="    " end="">
                    <item>return <xsl:value-of select="@type"/>.<xsl:value-of select="$unit-const"/></item>
                </list>
            </list>
        </xsl:for-each>

        <!-- Add __init__ method -->
        <xsl:variable name="unit-const" select="if (a:Enumerated[@name='unit']/@constant = '' or a:Enumerated[@name='unit']/@constant = 'none') then 'none' else a:Enumerated[@name='unit']/@constant"/>
        <list begin="" indent="    " end="">
            <item>def __init__(self, value, input_unit: str='<xsl:value-of select="$unit-const"/>', input_multiplier: str=None):</item>
            <list begin="" indent="    " end="">
                <item>self.__pint__(value=value, input_unit=input_unit, input_multiplier=input_multiplier)</item>
            </list>
        </list>

        <item/>
    </xsl:template>

    <!-- Generate attribute metadata -->
    <xsl:template name="generate_attribute_metadata">
        <item>'type': '<xsl:value-of select="if (a:Stereotype/@label) then a:Stereotype/@label else 'Attribute'"/>',</item>
        <item>'minOccurs': '<xsl:value-of select="(@minOccurs, '0')[1]"/>',</item>
        <item>'maxOccurs': '<xsl:value-of select="(@maxOccurs, '1')[1]"/>',</item>
        <item>'namespace': '<xsl:value-of select="substring-before((@baseProperty, '#')[1],'#')"/>#',</item>
        <!-- Uncomment lines below to include docstring in attribute metadata (for AI training, etc.)-->
        <!-- <item> 'docstring': </item> -->
        <!-- <xsl:call-template name="generate_class_docstring"/> -->
    </xsl:template>

    <!-- Generate association metadata -->
    <xsl:template name="generate-association-metadata">
        <xsl:if test="a:Stereotype/@label">
            <item> 'type': '<xsl:value-of select="a:Stereotype/@label"/>', </item>
        </xsl:if>
        <xsl:if test="not(a:Stereotype/@label)">
            <item> 'type': 'Attribute', </item>
        </xsl:if>
        <item>'minOccurs': '<xsl:value-of select="(@minOccurs, '0')[1]"/>',</item>
        <item>'maxOccurs': '<xsl:value-of select="(@maxOccurs, '1')[1]"/>',</item>
        <item>'inverse': '<xsl:value-of select="substring-after((@inverseBaseProperty, '#')[1],'#')"/>',</item>
        <item>'namespace': '<xsl:value-of select="substring-before((@baseProperty, '#')[1],'#')"/>#',</item>
        <!-- Uncomment lines below to include docstring in attribute metadata (for AI training, etc.)-->
        <!-- <item> 'docstring': </item> -->
        <!-- <xsl:call-template name="generate_class_docstring"/> -->
    </xsl:template>

    <!-- Generate inverse association metadata -->
    <xsl:template name="generate_inverse_association_metadata">
        <item>'type': '<xsl:value-of select="if (a:Stereotype/@label) then a:Stereotype/@label else 'Association'"/>',</item>
        <item>'minOccurs': '<xsl:value-of select="(@minOccurs, '0')[1]"/>',</item>
        <item>'maxOccurs': '<xsl:value-of select="(@maxOccurs, '1')[1]"/>',</item>
        <item>'inverse': '<xsl:value-of select="substring-after(@inverseBaseProperty, '#')"/>',</item>
        <item>'namespace': '<xsl:value-of select="substring-before(@baseProperty,'#')"/>#',</item>
        <!-- Uncomment lines below to include docstring in attribute metadata (for AI training, etc.)-->
        <!-- <item> 'docstring': </item> -->
        <!-- <xsl:call-template name="generate_class_docstring"/> -->
    </xsl:template>

    <!-- Function to get Python type mapping using explicit choose/when -->
    <xsl:function name="local:get_python_type" as="xs:string">
        <xsl:param name="xstype" as="xs:string?"/>
        <xsl:choose>
            <xsl:when test="not($xstype) or string-length($xstype) = 0">str</xsl:when>
            <xsl:when test="$xstype = 'string' or $xstype = 'String'">str</xsl:when>
            <xsl:when test="$xstype = 'integer' or $xstype = 'Integer' or $xstype = 'int'">int</xsl:when>
            <xsl:when test="$xstype = 'float' or $xstype = 'Float'">float</xsl:when>
            <xsl:when test="$xstype = 'double' or $xstype = 'Double'">float</xsl:when>
            <xsl:when test="$xstype = 'boolean' or $xstype = 'Boolean'">bool</xsl:when>
            <xsl:otherwise>str</xsl:otherwise>
        </xsl:choose>
    </xsl:function>

    <!-- Function to sanitize names with proper null handling -->
    <xsl:function name="local:sanitize_name" as="xs:string">
        <xsl:param name="name" as="xs:string"/>
        <xsl:param name="type" as="xs:string"/>

        <!-- Handle EAID_ prefixed names -->
        <xsl:variable name="clean_name" select="
            if (contains($name, 'EAID_')) then $type
            else replace($name, '[^a-zA-Z0-9_]', '')"/>

        <!-- Handle empty names -->
        <xsl:variable name="safe_name" select="
            if (string-length($clean_name) = 0) then 'unnamed'
            else $clean_name"/>

        <!-- Handle names starting with digits -->
        <xsl:variable name="prefixed-name" select="
            if (matches($safe_name, '^[0-9]')) then concat('_', $safe_name)
            else $safe_name"/>

        <!-- Handle Python keywords -->
        <xsl:sequence select="
            if ($prefixed-name = $python_keywords) then concat('_', $prefixed-name)
            else $prefixed-name"/>
    </xsl:function>

    <!-- Template to generate CIMStereotype enum from all stereotypes in the document -->
    <xsl:template name="generate_cim_stereotype_enum">

        <xsl:variable name="all_stereotypes" as="xs:string*">
            <xsl:for-each-group select="//a:Stereotype[local:sanitize_name(@label, @label)]" group-by="@label">
                <xsl:sort select="local:sanitize_name(@label, @label)"/>
                <xsl:sequence select="local:sanitize_name(@label, @label)"/>
            </xsl:for-each-group>
        </xsl:variable>

        <xsl:if test="exists($all_stereotypes)">
            <item>class CIMStereotype(Enum):</item>
            <list begin="" indent="    " end="">
                <xsl:for-each select="$all_stereotypes">
                    <item><xsl:value-of select="."/> = "<xsl:value-of select="."/>"</item>
                </xsl:for-each>
            </list>
            <item/>
        </xsl:if>
    </xsl:template>

</xsl:stylesheet>
