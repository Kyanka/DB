<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="//data">
        <html>
            <head>
                <title>Task4</title>
                <style type="text/css">
                    .wrapper {
                        padding: 20px;
                        display: grid;
                        grid-template-columns: repeat(5, 1fr);
                        gap: 20px;

                        font-family: sans-serif;
                    }

                    .good {
                        padding: 20px;
                        border: 1px solid #000;

                        display: flex;
                        flex-direction: column;
                        align-items: center;
                    }

                    .image {
                        margin: 10px;
                        padding: 5px;
                        border: 1px solid #ccc
                    }

                    .name {
                        margin-top: 10px;
                        font-style: italic;
                    }
                </style>
            </head>
            <body>
                <div class="wrapper">
                    <xsl:for-each select="//good">
                        <div class="good">
                            <img class="image">
                                <xsl:attribute name="src">
                                    <xsl:value-of select="./image"/>
                                </xsl:attribute>
                            </img>
                            <span class="name">
                                <xsl:value-of select="./name"/>
                            </span>
                            <p class="price">
                                <xsl:value-of select="./price"/>
                            </p>
                        </div>
                    </xsl:for-each>
                </div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>