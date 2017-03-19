<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
  xmlns:pkg="http://schemas.microsoft.com/office/2006/xmlPackage" 
  xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" 
  xmlns:mo="http://schemas.microsoft.com/office/mac/office/2008/main" 
  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" 
  xmlns:mv="urn:schemas-microsoft-com:mac:vml" 
  xmlns:o="urn:schemas-microsoft-com:office:office" 
  xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" 
  xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" 
  xmlns:v="urn:schemas-microsoft-com:vml" 
  xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" 
  xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" 
  xmlns:w10="urn:schemas-microsoft-com:office:word" 
  xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" 
  xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" 
  xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup"
  xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" 
  xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml"
  xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" 
  exclude-result-prefixes="xsl pkg wpc mo mc mv o r m v wp14 wp w10 w w14 wpg wpi wne wps">

  <xsl:template match="/">
    <xsl:apply-templates select="//w:document"/>
  </xsl:template>
  <xsl:template match="w:document/w:body">
    <document>
      <xsl:apply-templates select="w:p"/>
    </document>
  </xsl:template>

  <xsl:template match="w:p">
      <xsl:variable name="paragraph">
        <xsl:copy-of select="w:r/w:t"/>
      </xsl:variable>
      <xsl:if test="not($paragraph = '')">
        <section>
          <position><xsl:value-of select="position()"/></position>
          <type>
            <xsl:value-of select="w:pPr/w:pStyle/@w:val"/>
          </type>
          <content>
            <xsl:value-of select="$paragraph"/>
          </content>
        </section>
      </xsl:if>
  </xsl:template>

</xsl:stylesheet>
