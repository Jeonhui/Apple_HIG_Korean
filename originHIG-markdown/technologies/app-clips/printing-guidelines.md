# **[technologies-app-clips] printing-guidelines**

App Clip Codes offer the best experience to launch App Clips. As a result, it’s important to manufacture and display App Clip Codes that offer a reliable scanning experience for a long time. You can print App Clip Codes yourself, or work with a professional printing service — for example, [RR Donnelley](https://touchless.acc.rrd.com/).

Always test printed App Clip Codes before you distribute them to be sure they’re scannable from a variety of angles.

**Use high-quality, non-textured print materials.** Print App Clip Codes on matte finishes. Avoid shine, gloss, reflective or holographic overlays, as well as thin laminate finishes or materials. In case you need to laminate print material with an App Clip Code on it, use a matte laminate to avoid shine and reflections. If you place your App Clip Code outdoors, use UV-resistant materials or coatings to prevent fading from exposure to sunlight, rain, and other weather conditions. If you work with a professional printing service, use flexographic printing for best results. If you print the App Clip Codes yourself using a desktop printer, use an inkjet printer for best results.

**Use high-resolution images and printer settings.** When rasterizing the SVG file, set the image resolution to at least 600 ppi, and print your App Clip Codes with a minimum resolution of 300 dpi. Consider leveling and calibrating your printer before printing to ensure a high print quality, and avoid poor color channel alignment, inaccurate gamma values, artifacts, or printing elliptical or otherwise distorted App Clip Codes. When using receipt printers, print App Clip Codes as close to the paper’s maximum bounds as possible.

**Use correct color settings when you convert the generated SVG file to a CMYK image.** Both the [App Clip Code Generator](https://developer.apple.com/app-clips/resources/) command-line tool and [App Store Connect](https://appstoreconnect.apple.com/) generate App Clip Codes as SVG files in the sRGB color space. To print colors that match the SVG file, convert the sRGB image to a CMYK image. Use a relative calorimetric (media-relative) intent when performing the conversion. Use "Generic CMYK ICC profile" on CMYK printers or "Gracol 2013 ICC profile" on CMYKOV printers and allow for a color tolerance CIELab Delta E of 2.5.

**If you’re using a printer that only prints in grayscale, only generate grayscale App Clip Codes.** Codes generated in color and then printed in grayscale may work less reliably.

**For NFC-integrated App Clip Codes, choose Type 5 NFC tags.** The embedded NFC tag should be at least 35 mm in diameter or of equivalent size.

**If you create large batches of App Clip Codes, thoroughly test your printing workflow, and verify printed App Clip Codes.** For example, conduct small, inexpensive print runs using a subset of codes. Print your App Clip Codes on print templates with additional padded regions that allow you to display the encoded invocation URL and the SVG filename alongside each code for validation at the time of print.

If you create many App Clip Codes with the [App Clip Code Generator](https://developer.apple.com/app-clips/resources/) tool or [App Store Connect](https://appstoreconnect.apple.com/), you’ll likely work with a professional printing service. If this is the case, you need to handle a lot of SVG files. Because you have no way of knowing which App Clip Code encodes which URL by looking at an App Clip Code, you need to use a file that contains information about which SVG file maps to which invocation URL. Under any circumstance, careful file management, versioning, and change tracking are key to avoiding faulty print runs. For more information, see [Preparing Multiple App Clip Codes for Production](https://developer.apple.com/documentation/app_clips/preparing_multiple_app_clip_codes_for_production).

# **Verifying your printer’s calibration**

A reliable scanning experience depends on the quality of your printed App Clip Codes. To ensure printing App Clip Codes results in a reliable scanning experience and to avoid using a printer that can’t print high-quality App Clip Codes, Apple offers [printer calibration test sheets](https://developer.apple.com/app-clips/resources/printer-calibration-test-sheets.zip) you can use to verify your printer’s settings and print quality.

**Verify print quality of your chosen color pair with the printer calibration test sheet that shows text boxes for each default color pair.** Follow the instructions on the sheet to print it at the right scale and to verify that your printer can create high-quality App Clip Codes.

**Verify your printer’s grayscale settings by printing the printer calibration test sheet that shows two grayscale bars.** If any of the specific gray colors are light or entirely missing, the printer may need calibration or may not be suitable for printing an App Clip Code that allows for reliable scanning.