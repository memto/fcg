PAGE_PLACEHOLDER = """<!-- PAGE_PLACEHOLDER -->"""
FRONT_CEL_PLACEHOLDER = """<!-- FRONT_CEL_PLACEHOLDER -->"""
BACK_CEL_PLACEHOLDER = """<!-- BACK_CEL_PLACEHOLDER -->"""

PAGE_TMP_PLACEHOLDER = """         <table:table table:name="{frontTableName}" table:style-name="Table1">
            <table:table-column table:style-name="Table1.A" />
            <table:table-column table:style-name="Table1.B" />
            <table:table-row table:style-name="Table1.1">
               <table:table-cell table:style-name="Table1.A1" office:value-type="string">
                  <text:p text:style-name="Table_20_Contents">
                     <!-- FRONT_CEL_PLACEHOLDER -->
                  </text:p>
               </table:table-cell>
               <table:table-cell table:style-name="Table1.B1" office:value-type="string">
                  <text:p text:style-name="Table_20_Contents">
                     <!-- FRONT_CEL_PLACEHOLDER -->
                  </text:p>
               </table:table-cell>
            </table:table-row>
            <table:table-row table:style-name="Table1.1">
               <table:table-cell table:style-name="Table1.A2" office:value-type="string">
                  <text:p text:style-name="Table_20_Contents">
                     <!-- FRONT_CEL_PLACEHOLDER -->
                  </text:p>
               </table:table-cell>
               <table:table-cell table:style-name="Table1.B2" office:value-type="string">
                  <text:p text:style-name="Table_20_Contents">
                     <!-- FRONT_CEL_PLACEHOLDER -->
                  </text:p>
               </table:table-cell>
            </table:table-row>
         </table:table>

         <table:table table:name="{backTableName}" table:style-name="Table2">
            <table:table-column table:style-name="Table2.A" />
            <table:table-column table:style-name="Table2.B" />
            <text:soft-page-break />
            <table:table-row table:style-name="Table2.1">
               <table:table-cell table:style-name="Table2.A1" office:value-type="string">
                  <!-- BACK_CEL_PLACEHOLDER -->                  
                  <text:p text:style-name="Table_20_Contents" />
               </table:table-cell>
               <table:table-cell table:style-name="Table2.B1" office:value-type="string">
                  <!-- BACK_CEL_PLACEHOLDER -->                  
                  <text:p text:style-name="Table_20_Contents" />
               </table:table-cell>
            </table:table-row>
            <table:table-row table:style-name="Table2.1">
               <table:table-cell table:style-name="Table2.A2" office:value-type="string">
                  <!-- BACK_CEL_PLACEHOLDER -->                  
                  <text:p text:style-name="Table_20_Contents" />
               </table:table-cell>
               <table:table-cell table:style-name="Table2.B2" office:value-type="string">
                  <!-- BACK_CEL_PLACEHOLDER -->                  
                  <text:p text:style-name="Table_20_Contents" />
               </table:table-cell>
            </table:table-row>
         </table:table>

"""

FRONT_CEL_TMP = """                     <draw:frame draw:style-name="fr1" draw:name="{imageName}" text:anchor-type="as-char" svg:width="5.5in" svg:height="4in" draw:z-index="0">
                        <draw:image xlink:href="Pictures/{imageName}" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" />
                     </draw:frame>"""

BACK_CEL_TMP = """                  <table:table table:name="Table3" table:style-name="Table3">
                     <table:table-column table:style-name="Table3.A" />
                     <table:table-column table:style-name="Table3.B" />
                     <table:table-row table:style-name="Table3.1">
                        <table:table-cell table:style-name="Table3.A1" table:number-columns-spanned="2" office:value-type="string">
                           <text:p text:style-name="P4">{header}</text:p>
                           <text:p text:style-name="P5">
                              <text:span text:style-name="T1">(</text:span>
                              by Dad with &lt;3
                              <text:span text:style-name="T2">)</text:span>
                           </text:p>
                        </table:table-cell>
                        <table:covered-table-cell />
                     </table:table-row>
                     <table:table-row table:style-name="Table3.1">
                        <table:table-cell table:style-name="Table3.A2" office:value-type="string">
                           <text:p text:style-name="P2">{text0}</text:p>
                        </table:table-cell>
                        <table:table-cell table:style-name="Table3.A2" office:value-type="string">
                           <text:p text:style-name="P2">{text1}</text:p>
                        </table:table-cell>
                     </table:table-row>
                     <table:table-row table:style-name="Table3.1">
                        <table:table-cell table:style-name="Table3.A2" office:value-type="string">
                           <text:p text:style-name="P2">{text2}</text:p>
                        </table:table-cell>
                        <table:table-cell table:style-name="Table3.A2" office:value-type="string">
                           <text:p text:style-name="P2">{text3}</text:p>
                        </table:table-cell>
                     </table:table-row>
                     <table:table-row table:style-name="Table3.1">
                        <table:table-cell table:style-name="Table3.A2" office:value-type="string">
                           <text:p text:style-name="P2">{text4}</text:p>
                        </table:table-cell>
                        <table:table-cell table:style-name="Table3.A2" office:value-type="string">
                           <text:p text:style-name="P2">{text5}</text:p>
                        </table:table-cell>
                     </table:table-row>
                     <table:table-row table:style-name="Table3.1">
                        <table:table-cell table:style-name="Table3.A2" office:value-type="string">
                           <text:p text:style-name="P2">{text6}</text:p>
                        </table:table-cell>
                        <table:table-cell table:style-name="Table3.A2" office:value-type="string">
                           <text:p text:style-name="P2">{text7}</text:p>
                        </table:table-cell>
                     </table:table-row>
                     <table:table-row table:style-name="Table3.1">
                        <table:table-cell table:style-name="Table3.A2" office:value-type="string">
                           <text:p text:style-name="P2">{text8}</text:p>
                        </table:table-cell>
                        <table:table-cell table:style-name="Table3.A2" office:value-type="string">
                           <text:p text:style-name="P2">{text9}</text:p>
                        </table:table-cell>
                     </table:table-row>
                     <table:table-row table:style-name="Table3.1">
                        <table:table-cell table:style-name="Table3.A2" office:value-type="string">
                           <text:p text:style-name="P2">{text10}</text:p>
                        </table:table-cell>
                        <table:table-cell table:style-name="Table3.A2" office:value-type="string">
                           <text:p text:style-name="P2">{text11}</text:p>
                        </table:table-cell>
                     </table:table-row>
                     <table:table-row table:style-name="Table3.1">
                        <table:table-cell table:style-name="Table3.A8" table:number-columns-spanned="2" office:value-type="string">
                           <text:p text:style-name="P1">{footer}</text:p>
                        </table:table-cell>
                        <table:covered-table-cell />
                     </table:table-row>
                  </table:table>"""
