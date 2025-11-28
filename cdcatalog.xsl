<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:fo="http://www.w3.org/1999/XSL/Format">
                
                <xsl:template match="/">
    <fo:root>
      <fo:layout-master-set>
        <fo:simple-page-master master-name="A4-portrait"
                               page-height="29.7cm" page-width="21cm"
                               margin-top="2cm" margin-bottom="2cm"
                               margin-left="2.5cm" margin-right="2.5cm">
                               <fo:region-body margin-top="1.5cm"/>
          <fo:region-before extent="1.5cm"/>
          <fo:region-after extent="1.5cm"/>
          </fo:simple-page-master>
        </fo:layout-master-set>
      
      <fo:page-sequence master-reference="A4-portrait"> 
        <fo:flow flow-name="xsl-region-body"> 
          <xsl:apply-templates select="customers/customer"/> 
          </fo:flow>
        </fo:page-sequence> 
      </fo:root>
    </xsl:template>
  
  <xsl:template match="customer">
    <fo:block-container space-after="0.7cm" 
                        border-top="1pt solid #CCCCCC" 
                        padding-top="5pt"
                        break-before="page"> 
      
      <fo:block font-family="sans-serif" font-size="12pt" font-weight="bold" space-after="0.2cm">
        <xsl:value-of select="normalize-space(name)"/>
        </fo:block>
      <fo:block font-family="sans-serif" font-size="12pt" font-weight="bold" text-align="center" space-after="0.2cm" >
        <xsl:value-of select="normalize-space(text)"/>
      </fo:block>
      <fo:block>
        <fo:table width="110mm" border-style="ridge" border-width="5pt">       (1)                        
          <fo:table-body>                                                     (2)
            <fo:table-row>                                                   (3)
              <fo:table-cell width="40mm" border-style="solid" border-width="1pt"> (4)
                <fo:block>  <xsl:value-of select="normalize-space(name)"/></fo:block>                         
              </fo:table-cell>                         
              <fo:table-cell width="40mm" border-style="solid" border-width="1pt"> (4)
                <fo:block> <xsl:value-of select="normalize-space(town)"/></fo:block>
              </fo:table-cell>
              <fo:table-cell width="30mm" border-style="solid" border-width="1pt"> (4)
                <fo:block> 3. Zelle</fo:block>                         
              </fo:table-cell>                         
            </fo:table-row>                                                 (3)
            <fo:table-row>
              <fo:table-cell border-style="solid" border-width="1pt">      (5)
                <fo:block> 1. Zelle</fo:block>
              </fo:table-cell>
            
            </fo:table-row>
          </fo:table-body>
        </fo:table>
      </fo:block>
      </fo:block-container>

    </xsl:template>
  
 
  
</xsl:stylesheet>