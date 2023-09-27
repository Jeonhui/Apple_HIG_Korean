June 21, 2023

 Updated to include guidance for visionOS. Typography
==========

In addition to ensuring legible text, your typographic choices can help you clarify an information hierarchy, communicate important content, and express your brand.![A sketch of a small letter A to the left of a large letter A, suggesting the use of typography to convey hierarchical information. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/d90940d120149af7220e4fedfd1c10bd/foundations-typography-intro@2x.png)

[Best practices](/design/human-interface-guidelines/typography#Best-practices)
------------------------------------------------------------------------------

**Strive to maintain a minimum font size that most people can read easily.** Differences in device displays, including pixel density and brightness, can influence the appropriate minimum font size. Other factors, such as the reader’s proximity to the text, their visual acuity and whether they’re in motion, and ambient lighting, can all impact legibility. When you support Dynamic Type — a feature that lets people choose the size of visible text in iOS, iPadOS, tvOS, visionOS, and watchOS — your app or game can respond appropriately when people adjust text to a size that works for them. For developer guidance, see [Text input and output](/documentation/SwiftUI/Text-input-and-output)
; for available sizes, see [Specifications](/design/human-interface-guidelines/typography#Specifications)
.

**Adjust font weight, size, and color as needed to emphasize important information and help people visualize hierarchy.** Be sure to maintain the relative hierarchy and visual distinction of text elements when people adjust text sizes.

**Minimize the number of typefaces you use in your interface.** Mixing too many different typefaces can obscure your information hierarchy and hinder readability.

**Test legibility in different contexts.** For example, in addition to adjusting text size, people may read your content outside in bright sunlight, glance at it while they’re in motion, or view it from a distance. If testing shows that some of your text is difficult to read, consider modifying the text or background colors to increase contrast, using a larger type size, or using typefaces designed for optimized legibility, like the system fonts.

**In general, avoid light font weights to help maintain readability.** For example, if you’re using system-provided fonts, prefer Medium, Semibold, or Bold font weights, and avoid Ultralight, Thin, and Light font weights, which can be difficult to see, especially when text is small. In general, use Regular sparingly.

**Prioritize important content when responding to text-size changes.** Not all content is equally important. When someone chooses a larger text size, they typically want to make the content they care about easier to read; they don’t always want to increase the size of every word on the screen. For example, when people choose a large accessibility text size, Mail displays the subject and body of the message in the large size, but leaves less important text — such as the date and the sender — in a smaller size.

[Using system fonts](/design/human-interface-guidelines/typography#Using-system-fonts)
--------------------------------------------------------------------------------------

Apple provides two typeface families that support an extensive range of weights, sizes, styles, and languages.

**San Francisco (SF)** is a sans serif typeface family that includes the SF Pro, SF Compact, SF Arabic, and SF Mono variants.

![The phrase 'The quick brown fox jumps over the lazy dog.' shown in the San Francisco Pro font.](https://docs-assets.developer.apple.com/published/f58cfb3efe1bd20e414f862e1db94136/sanfrancisco@2x.png)

The system also offers the SF Pro Rounded, SF Arabic Rounded, and SF Compact Rounded variants you can use to coordinate text with the appearance of soft or rounded UI elements, or to provide an alternative typographic voice.

**New York (NY)** is a serif typeface family designed to work well by itself and alongside the SF fonts.

![The phrase 'The quick brown fox jumps over the lazy dog.' shown in the New York font.](https://docs-assets.developer.apple.com/published/c9d59e62ef6005500335ef95aa28152e/new-york@2x.png)

You can download the San Francisco and New York fonts [here](https://developer.apple.com/fonts/)
.

The system provides the SF and NY fonts in the *variable* font format, which combines different font styles together in one file, and supports interpolation between styles to create intermediate ones.

Note

Variable fonts support *optical sizing*, which refers to the adjustment of different typographic designs to fit different sizes. On all platforms, the system fonts support *dynamic optical sizes*, which merge discrete optical sizes (like Text and Display) and weights into a single, continuous design, letting the system interpolate each glyph or letterform to produce a structure that’s precisely adapted to the point size. With dynamic optical sizes, you don’t need to use discrete optical sizes unless you’re working with a design tool that doesn’t support all the features of the variable font format.

To help you define visual hierarchies and create clear and legible designs in many different sizes and contexts, the system fonts are available in a variety of weights, ranging from Ultralight to Black, and — in the case of SF — several widths, including Condensed and Expanded. Because SF Symbols use equivalent weights, you can achieve precise weight matching between symbols and adjacent text, regardless of the size or style you choose.

Note

[SF Symbols](/design/human-interface-guidelines/sf-symbols)
 provides a comprehensive library of symbols that integrate seamlessly with the San Francisco system font, automatically aligning with text in all weights and sizes. Consider using symbols when you need to convey a concept or depict an object, especially within text.

The system defines a set of typographic attributes — called text styles — that work with both typeface families. A *text style* specifies a combination of font weight, point size, and leading values for each text size. For example, the *body* text style uses values that support a comfortable reading experience over multiple lines of text, while the *headline* style assigns a font size and weight that help distinguish a heading from surrounding content. Taken together, the text styles form a typographic hierarchy you can use to express the different levels of importance in your content. Text styles also allow text to scale proportionately when people change the system’s text size or make accessibility adjustments, like turning on Larger Text in Accessibility settings.

**Consider using the built-in text styles.** The system-defined text styles give you a convenient and consistent way to convey your information hierarchy through font size and weight. Using text styles with the system fonts also supports Dynamic Type and the larger accessibility type sizes (where available), which let people choose the text size that works for them.

**Modify the built-in text styles if necessary.** System APIs define font adjustments — called *symbolic traits* — that let you modify some aspects of a text style. For example, the bold trait adds weight to text, letting you create another level of hierarchy. You can also use symbolic traits to adjust leading if you need to improve readability or conserve space. For example, when you display text in wide columns or long passages, more space between lines (*loose leading*) can make it easier for people to keep their place while moving from one line to the next. Conversely, if you need to display multiple lines of text in an area where height is constrained — for example, in a list row — decreasing the space between lines (*tight leading*) can help the text fit well. If you need to display three or more lines of text, avoid tight leading even in areas where height is limited. For developer guidance, see [leading(\_:)](https://developer.apple.com/documentation/swiftui/font/leading(_:))
.

**Adjust tracking as needed in interface mockups.** In a running app, the system font dynamically adjusts tracking at every point size. To produce an accurate interface mockup of an interface that uses the variable system fonts, you don’t have to choose a discrete optical size at certain point sizes, but you might need to adjust the tracking. For guidance, see [Specifications](/design/human-interface-guidelines/typography#Specifications)
.

Developer note

You can use the constants defined in [`Font.Design`](/documentation/SwiftUI/Font/Design)
 to access all system fonts — don’t embed system fonts in your app or game. For example, use [`Font.Design.default`](/documentation/SwiftUI/Font/Design/default)
 to get the system font on all platforms; use [`Font.Design.serif`](/documentation/SwiftUI/Font/Design/serif)
 to get the New York font.

[Using custom fonts](/design/human-interface-guidelines/typography#Using-custom-fonts)
--------------------------------------------------------------------------------------

**Make sure custom fonts are legible.** Unless your app has a compelling need for a custom font — such as for branding purposes or to create an immersive gaming experience — prefer the system fonts. If you do use a custom font, make sure people can read it easily at various viewing distances and under a variety of conditions.

**Implement accessibility features for custom fonts.** System fonts automatically support Dynamic Type (where available) and respond when people turn on accessibility features, such as Bold Text. If you use a custom font, make sure it implements the same behaviors. For developer guidance, see [Applying custom fonts to text](/documentation/SwiftUI/Applying-Custom-Fonts-to-Text)
.

[Platform considerations](/design/human-interface-guidelines/typography#Platform-considerations)
------------------------------------------------------------------------------------------------

### [iOS, iPadOS](/design/human-interface-guidelines/typography#iOS-iPadOS)

SF Pro is the system font in iOS and iPadOS. iOS and iPadOS apps can also use NY.

### [macOS](/design/human-interface-guidelines/typography#macOS)

SF Pro is the system font in macOS. NY is available for Mac apps built with Mac Catalyst. macOS doesn’t support Dynamic Type.

**When necessary, use dynamic system font variants to match the text in standard controls.** Dynamic system font variants give your text the same look and feel of the text that appears in system-provided controls. Use the variants listed below to achieve a look that’s consistent with other apps on the platform.



| Dynamic font variant | API |
| --- | --- |
| Control content | [`controlContentFont(ofSize:)`](/documentation/appkit/nsfont/1527070-controlcontentfont)
 |
| Label | [`labelFont(ofSize:)`](/documentation/appkit/nsfont/1528213-labelfont)
 |
| Menu | [`menuFont(ofSize:)`](/documentation/appkit/nsfont/1533068-menufont)
 |
| Menu bar | [`menuBarFont(ofSize:)`](/documentation/appkit/nsfont/1534194-menubarfont)
 |
| Message | [`messageFont(ofSize:)`](/documentation/appkit/nsfont/1525777-messagefont)
 |
| Palette | [`paletteFont(ofSize:)`](/documentation/appkit/nsfont/1535462-palettefont)
 |
| Title | [`titleBarFont(ofSize:)`](/documentation/appkit/nsfont/1530200-titlebarfont)
 |
| Tool tips | [`toolTipsFont(ofSize:)`](/documentation/appkit/nsfont/1527704-tooltipsfont)
 |
| Document text (user) | [`userFont(ofSize:)`](/documentation/appkit/nsfont/1524559-userfont)
 |
| Monospaced document text (user fixed pitch) | [`userFixedPitchFont(ofSize:)`](/documentation/appkit/nsfont/1531381-userfixedpitchfont)
 |
| Bold system font | [`boldSystemFont(ofSize:)`](/documentation/appkit/nsfont/1533549-boldsystemfont)
 |
| System font | [`systemFont(ofSize:)`](/documentation/appkit/nsfont/1530094-systemfont)
 |

### [tvOS](/design/human-interface-guidelines/typography#tvOS)

SF Pro is the system font in tvOS, and apps can also use NY.

### [visionOS](/design/human-interface-guidelines/typography#visionOS)

SF Pro is the system font in visionOS. If you use NY, you need to specify the type styles you want.

visionOS uses bolder versions of the Dynamic Type body and title styles and it introduces Extra Large Title 1 and Extra Large Title 2 for wide, editorial-style layouts. For guidance using vibrancy to indicate hierarchy in text and symbols, see [Materials > visionOS](/design/human-interface-guidelines/materials#visionOS)
.

**In general, prefer 2D text.** The more visual depth characters have, the more difficult they can be to read. Although a small amount of 3D text can provide a fun visual element that draws people’s attention, if you’re going to display content that people need to read and understand, prefer using text that has little or no visual depth.

![A screenshot that shows the correct placement of 2D text on a window in visionOS.](https://docs-assets.developer.apple.com/published/b7eca42cb50603b5ae1630781ce6d4c7/visionos-typography-2d-text-correct@2x.png)

![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![A screenshot that shows the incorrect placement of 3D text on a window in visionOS.](https://docs-assets.developer.apple.com/published/8568cd71b363e427fb91a874b8c30aa8/visionos-typography-3d-text-incorrect@2x.png)

![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

**Make sure text looks good and remains legible when people scale it.** Use a text style that makes the text look good at full scale, then test it for legibility at different scales.

**Maximize the contrast between text and the background of its container.** By default, the system displays text in white, because this color tends to provide a strong contrast with the default system background material, making text easier to read. If you want to use a different text color, be sure to test it in a variety of contexts.

**If you need to display text that’s not on a background, consider making it bold to improve legibility.** In this situation, you generally want to avoid adding shadows to increase text contrast. The current space might not include a visual surface on which to cast an accurate shadow, and you can’t predict the size and density of shadow that would work well with a person’s current Environment.

**Keep text facing people as much as possible.** If you display text that’s associated with a point in space, such as text that labels a 3D object, you generally want the text to face the wearer regardless of how they or the object move. For example, if you display a label that’s parallel to a visible line, you probably want the text to rotate around that line. If you display a label for a 3D object, you might want to make the label look like it’s printed on the object or parallel to its surface.

### [watchOS](/design/human-interface-guidelines/typography#watchOS)

SF Compact is the system font in watchOS, and apps can also use NY. In complications, watchOS uses SF Compact Rounded.

[Specifications](/design/human-interface-guidelines/typography#Specifications)
------------------------------------------------------------------------------

### [iOS, iPadOS Dynamic Type sizes](/design/human-interface-guidelines/typography#iOS-iPadOS-Dynamic-Type-sizes)

* [xSmall](#)
* [Small](#)
* [Medium](#)
* [Large (Default)](#)
* [xLarge](#)
* [xxLarge](#)
* [xxxLarge](#)
#### [xSmall](/design/human-interface-guidelines/typography#xSmall)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 31 | 38 |
| Title 1 | Regular | 25 | 31 |
| Title 2 | Regular | 19 | 24 |
| Title 3 | Regular | 17 | 22 |
| Headline | Semibold | 14 | 19 |
| Body | Regular | 14 | 19 |
| Callout | Regular | 13 | 18 |
| Subhead | Regular | 12 | 16 |
| Footnote | Regular | 12 | 16 |
| Caption 1 | Regular | 11 | 13 |
| Caption 2 | Regular | 11 | 13 |

Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

#### [Small](/design/human-interface-guidelines/typography#Small)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 32 | 39 |
| Title 1 | Regular | 26 | 32 |
| Title 2 | Regular | 20 | 25 |
| Title 3 | Regular | 18 | 23 |
| Headline | Semibold | 15 | 20 |
| Body | Regular | 15 | 20 |
| Callout | Regular | 14 | 19 |
| Subhead | Regular | 13 | 18 |
| Footnote | Regular | 12 | 16 |
| Caption 1 | Regular | 11 | 13 |
| Caption 2 | Regular | 11 | 13 |

Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

#### [Medium](/design/human-interface-guidelines/typography#Medium)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 33 | 40 |
| Title 1 | Regular | 27 | 33 |
| Title 2 | Regular | 21 | 26 |
| Title 3 | Regular | 19 | 24 |
| Headline | Semibold | 16 | 21 |
| Body | Regular | 16 | 21 |
| Callout | Regular | 15 | 20 |
| Subhead | Regular | 14 | 19 |
| Footnote | Regular | 12 | 16 |
| Caption 1 | Regular | 11 | 13 |
| Caption 2 | Regular | 11 | 13 |

Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

#### [Large (Default)](/design/human-interface-guidelines/typography#Large-Default)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 34 | 41 |
| Title 1 | Regular | 28 | 34 |
| Title 2 | Regular | 22 | 28 |
| Title 3 | Regular | 20 | 25 |
| Headline | Semibold | 17 | 22 |
| Body | Regular | 17 | 22 |
| Callout | Regular | 16 | 21 |
| Subhead | Regular | 15 | 20 |
| Footnote | Regular | 13 | 18 |
| Caption 1 | Regular | 12 | 16 |
| Caption 2 | Regular | 11 | 13 |

Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

#### [xLarge](/design/human-interface-guidelines/typography#xLarge)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 36 | 43 |
| Title 1 | Regular | 30 | 37 |
| Title 2 | Regular | 24 | 30 |
| Title 3 | Regular | 22 | 28 |
| Headline | Semibold | 19 | 24 |
| Body | Regular | 19 | 24 |
| Callout | Regular | 18 | 23 |
| Subhead | Regular | 17 | 22 |
| Footnote | Regular | 15 | 20 |
| Caption 1 | Regular | 14 | 19 |
| Caption 2 | Regular | 13 | 18 |

Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

#### [xxLarge](/design/human-interface-guidelines/typography#xxLarge)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 38 | 46 |
| Title 1 | Regular | 32 | 39 |
| Title 2 | Regular | 26 | 32 |
| Title 3 | Regular | 24 | 30 |
| Headline | Semibold | 21 | 26 |
| Body | Regular | 21 | 26 |
| Callout | Regular | 20 | 25 |
| Subhead | Regular | 19 | 24 |
| Footnote | Regular | 17 | 22 |
| Caption 1 | Regular | 16 | 21 |
| Caption 2 | Regular | 15 | 20 |

Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

#### [xxxLarge](/design/human-interface-guidelines/typography#xxxLarge)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 40 | 48 |
| Title 1 | Regular | 34 | 41 |
| Title 2 | Regular | 28 | 34 |
| Title 3 | Regular | 26 | 32 |
| Headline | Semibold | 23 | 29 |
| Body | Regular | 23 | 29 |
| Callout | Regular | 22 | 28 |
| Subhead | Regular | 21 | 28 |
| Footnote | Regular | 19 | 24 |
| Caption 1 | Regular | 18 | 23 |
| Caption 2 | Regular | 17 | 22 |

Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

### [iOS, iPadOS larger accessibility type sizes](/design/human-interface-guidelines/typography#iOS-iPadOS-larger-accessibility-type-sizes)

* [AX1](#)
* [AX2](#)
* [AX3](#)
* [AX4](#)
* [AX5](#)
#### [AX1](/design/human-interface-guidelines/typography#AX1)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 44 | 52 |
| Title 1 | Regular | 38 | 46 |
| Title 2 | Regular | 34 | 41 |
| Title 3 | Regular | 31 | 38 |
| Headline | Semibold | 28 | 34 |
| Body | Regular | 28 | 34 |
| Callout | Regular | 26 | 32 |
| Subhead | Regular | 25 | 31 |
| Footnote | Regular | 23 | 29 |
| Caption 1 | Regular | 22 | 28 |
| Caption 2 | Regular | 20 | 25 |

Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

#### [AX2](/design/human-interface-guidelines/typography#AX2)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 48 | 57 |
| Title 1 | Regular | 43 | 51 |
| Title 2 | Regular | 39 | 47 |
| Title 3 | Regular | 37 | 44 |
| Headline | Semibold | 33 | 40 |
| Body | Regular | 33 | 40 |
| Callout | Regular | 32 | 39 |
| Subhead | Regular | 30 | 37 |
| Footnote | Regular | 27 | 33 |
| Caption 1 | Regular | 26 | 32 |
| Caption 2 | Regular | 24 | 30 |

Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

#### [AX3](/design/human-interface-guidelines/typography#AX3)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 52 | 61 |
| Title 1 | Regular | 48 | 57 |
| Title 2 | Regular | 44 | 52 |
| Title 3 | Regular | 43 | 51 |
| Headline | Semibold | 40 | 48 |
| Body | Regular | 40 | 48 |
| Callout | Regular | 38 | 46 |
| Subhead | Regular | 36 | 43 |
| Footnote | Regular | 33 | 40 |
| Caption 1 | Regular | 32 | 39 |
| Caption 2 | Regular | 29 | 35 |

Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

#### [AX4](/design/human-interface-guidelines/typography#AX4)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 56 | 66 |
| Title 1 | Regular | 53 | 62 |
| Title 2 | Regular | 50 | 59 |
| Title 3 | Regular | 49 | 58 |
| Headline | Semibold | 47 | 56 |
| Body | Regular | 47 | 56 |
| Callout | Regular | 44 | 52 |
| Subhead | Regular | 42 | 50 |
| Footnote | Regular | 38 | 46 |
| Caption 1 | Regular | 37 | 44 |
| Caption 2 | Regular | 34 | 41 |

Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

#### [AX5](/design/human-interface-guidelines/typography#AX5)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 60 | 70 |
| Title 1 | Regular | 58 | 68 |
| Title 2 | Regular | 56 | 66 |
| Title 3 | Regular | 55 | 65 |
| Headline | Semibold | 53 | 62 |
| Body | Regular | 53 | 62 |
| Callout | Regular | 51 | 60 |
| Subhead | Regular | 49 | 58 |
| Footnote | Regular | 44 | 52 |
| Caption 1 | Regular | 43 | 51 |
| Caption 2 | Regular | 40 | 48 |

Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

### [iOS, iPadOS tracking values](/design/human-interface-guidelines/typography#iOS-iPadOS-tracking-values)

* [SF Pro](#)
* [SF Pro Rounded](#)
* [New York](#)
#### [SF Pro](/design/human-interface-guidelines/typography#SF-Pro)



| Size (points) | Tracking (1/1000em) | Tracking (points) |
| --- | --- | --- |
| 6 | +41 | +0.24 |
| 7 | +34 | +0.23 |
| 8 | +26 | +0.21 |
| 9 | +19 | +0.17 |
| 10 | +12 | +0.12 |
| 11 | +6 | +0.06 |
| 12 | 0 | 0.0 |
| 13 | -6 | -0.08 |
| 14 | -11 | -0.15 |
| 15 | -16 | -0.23 |
| 16 | -20 | -0.31 |
| 17 | -26 | -0.43 |
| 18 | -25 | -0.44 |
| 19 | -24 | -0.45 |
| 20 | -23 | -0.45 |
| 21 | -18 | -0.36 |
| 22 | -12 | -0.26 |
| 23 | -4 | -0.10 |
| 24 | +3 | +0.07 |
| 25 | +6 | +0.15 |
| 26 | +8 | +0.22 |
| 27 | +11 | +0.29 |
| 28 | +14 | +0.38 |
| 29 | +14 | +0.40 |
| 30 | +14 | +0.40 |
| 31 | +13 | +0.39 |
| 32 | +13 | +0.41 |
| 33 | +12 | +0.40 |
| 34 | +12 | +0.40 |
| 35 | +11 | +0.38 |
| 36 | +10 | +0.37 |
| 37 | +10 | +0.36 |
| 38 | +10 | +0.37 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.37 |
| 41 | +9 | +0.36 |
| 42 | +9 | +0.37 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.35 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +7 | +0.33 |
| 50 | +7 | +0.34 |
| 51 | +7 | +0.35 |
| 52 | +6 | +0.33 |
| 53 | +6 | +0.31 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +5 | +0.28 |
| 60 | +4 | +0.26 |
| 62 | +4 | +0.24 |
| 64 | +4 | +0.22 |
| 66 | +3 | +0.19 |
| 68 | +2 | +0.17 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.14 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0 |
| 84 | 0 | 0 |
| 88 | 0 | 0 |
| 92 | 0 | 0 |
| 96 | 0 | 0 |

Not all apps express tracking values as 1/1000em. Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

#### [SF Pro Rounded](/design/human-interface-guidelines/typography#SF-Pro-Rounded)



| Size (Points) | Tracking (1/1000em) | Tracking (points) |
| --- | --- | --- |
| 6 | +87 | +0.51 |
| 7 | +80 | +0.54 |
| 8 | +72 | +0.57 |
| 9 | +65 | +0.57 |
| 10 | +58 | +0.57 |
| 11 | +52 | +0.56 |
| 12 | +46 | +0.54 |
| 13 | +40 | +0.51 |
| 14 | +35 | +0.48 |
| 15 | +30 | +0.44 |
| 16 | +26 | +0.41 |
| 17 | +22 | +0.37 |
| 18 | +21 | +0.37 |
| 19 | +20 | +0.37 |
| 20 | +18 | +0.36 |
| 21 | +17 | +0.35 |
| 22 | +16 | +0.34 |
| 23 | +16 | +0.35 |
| 24 | +15 | +0.35 |
| 25 | +14 | +0.35 |
| 26 | +14 | +0.36 |
| 27 | +14 | +0.36 |
| 28 | +13 | +0.36 |
| 29 | +13 | +0.37 |
| 30 | +12 | +0.37 |
| 31 | +12 | +0.36 |
| 32 | +12 | +0.38 |
| 33 | +12 | +0.39 |
| 34 | +12 | +0.38 |
| 35 | +11 | +0.38 |
| 36 | +11 | +0.39 |
| 37 | +10 | +0.38 |
| 38 | +10 | +0.39 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.39 |
| 41 | +10 | +0.38 |
| 42 | +10 | +0.39 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.37 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +8 | +0.36 |
| 50 | +7 | +0.34 |
| 51 | +6 | +0.32 |
| 52 | +6 | +0.33 |
| 53 | +6 | +0.31 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +4 | +0.25 |
| 60 | +4 | +0.23 |
| 62 | +4 | +0.21 |
| 64 | +3 | +0.19 |
| 66 | +2 | +0.16 |
| 68 | +2 | +0.13 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.11 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0.00 |
| 84 | 0 | 0.00 |
| 88 | 0 | 0.00 |
| 92 | 0 | 0.00 |
| 96 | 0 | 0.00 |

Not all apps express tracking values as 1/1000em. Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

#### [New York](/design/human-interface-guidelines/typography#New-York)



| Size (Points) | Tracking (1/1000em) | Tracking (points) |
| --- | --- | --- |
| 6 | +40 | +0.23 |
| 7 | +32 | +0.22 |
| 8 | +25 | +0.20 |
| 9 | +20 | +0.18 |
| 10 | +16 | +0.15 |
| 11 | +11 | +.12 |
| 12 | +6 | +0.07 |
| 13 | +4 | +0.05 |
| 14 | +2 | +0.03 |
| 15 | +0 | +0.00 |
| 16 | -2 | -0.03 |
| 17 | -4 | -0.07 |
| 18 | -6 | -0.11 |
| 19 | -8 | -0.15 |
| 20 | -10 | -0.20 |
| 21 | -10 | -0.21 |
| 22 | -10 | -0.23 |
| 23 | -11 | -0.25 |
| 24 | -11 | -0.26 |
| 25 | -11 | -0.27 |
| 26 | -12 | -0.29 |
| 27 | -12 | -0.32 |
| 28 | -12 | -0.33 |
| 29 | -12 | -0.34 |
| 30 | -12 | -0.37 |
| 31 | -13 | -0.39 |
| 32 | -13 | -0.41 |
| 33 | -13 | -0.42 |
| 34 | -14 | -0.45 |
| 35 | -14 | -0.48 |
| 36 | -14 | -0.49 |
| 38 | -14 | -0.52 |
| 40 | -14 | -0.55 |
| 42 | -14 | -0.57 |
| 44 | -14 | -0.62 |
| 46 | -14 | -0.65 |
| 48 | -14 | -0.68 |
| 50 | -14 | -0.71 |
| 52 | -14 | -0.74 |
| 54 | -15 | -0.79 |
| 58 | -15 | -0.85 |
| 62 | -15 | -0.91 |
| 66 | -15 | -0.97 |
| 70 | -16 | -1.06 |
| 72 | -16 | -1.09 |
| 80 | -16 | -1.21 |
| 88 | -16 | -1.33 |
| 96 | -16 | -1.50 |
| 100 | -16 | -1.56 |
| 120 | -16 | -1.88 |
| 140 | -16 | -2.26 |
| 160 | -16 | -2.58 |
| 180 | -17 | -2.99 |
| 200 | -17 | -3.32 |
| 220 | -18 | -3.76 |
| 240 | -18 | -4.22 |
| 260 | -18 | -4.57 |

Not all apps express tracking values as 1/1000em. Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

### [macOS built-in text styles](/design/human-interface-guidelines/typography#macOS-built-in-text-styles)



| Text style | Weight | Size (points) | Line height (points) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 26 | 32 | Bold |
| Title 1 | Regular | 22 | 26 | Bold |
| Title 2 | Regular | 17 | 22 | Bold |
| Title 3 | Regular | 15 | 20 | Semibold |
| Headline | Bold | 13 | 16 | Heavy |
| Body | Regular | 13 | 16 | Semibold |
| Callout | Regular | 12 | 15 | Semibold |
| Subheadline | Regular | 11 | 14 | Semibold |
| Footnote | Regular | 10 | 13 | Semibold |
| Caption 1 | Regular | 10 | 13 | Medium |
| Caption 2 | Medium | 10 | 13 | Semibold |

Point size based on image resolution of 144 ppi for @2x designs.

### [macOS tracking values](/design/human-interface-guidelines/typography#macOS-tracking-values)



| Size (points) | Tracking (1/1000em) | Tracking (points) |
| --- | --- | --- |
| 6 | +41 | +0.24 |
| 7 | +34 | +0.23 |
| 8 | +26 | +0.21 |
| 9 | +19 | +0.17 |
| 10 | +12 | +0.12 |
| 11 | +6 | +0.06 |
| 12 | 0 | 0.0 |
| 13 | -6 | -0.08 |
| 14 | -11 | -0.15 |
| 15 | -16 | -0.23 |
| 16 | -20 | -0.31 |
| 17 | -26 | -0.43 |
| 18 | -25 | -0.44 |
| 19 | -24 | -0.45 |
| 20 | -23 | -0.45 |
| 21 | -18 | -0.36 |
| 22 | -12 | -0.26 |
| 23 | -4 | -0.10 |
| 24 | +3 | +0.07 |
| 25 | +6 | +0.15 |
| 26 | +8 | +0.22 |
| 27 | +11 | +0.29 |
| 28 | +14 | +0.38 |
| 29 | +14 | +0.40 |
| 30 | +14 | +0.40 |
| 31 | +13 | +0.39 |
| 32 | +13 | +0.41 |
| 33 | +12 | +0.40 |
| 34 | +12 | +0.40 |
| 35 | +11 | +0.38 |
| 36 | +10 | +0.37 |
| 37 | +10 | +0.36 |
| 38 | +10 | +0.37 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.37 |
| 41 | +9 | +0.36 |
| 42 | +9 | +0.37 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.35 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +7 | +0.33 |
| 50 | +7 | +0.34 |
| 51 | +7 | +0.35 |
| 52 | +6 | +0.31 |
| 53 | +6 | +0.33 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +5 | +0.28 |
| 60 | +4 | +0.26 |
| 62 | +4 | +0.24 |
| 64 | +4 | +0.22 |
| 66 | +3 | +0.19 |
| 68 | +2 | +0.17 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.14 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0 |
| 84 | 0 | 0 |
| 88 | 0 | 0 |
| 92 | 0 | 0 |
| 96 | 0 | 0 |

Not all apps express tracking values as 1/1000em. Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

### [tvOS Dynamic Type sizes](/design/human-interface-guidelines/typography#tvOS-Dynamic-Type-sizes)



| Style (standard) | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Title 1 | Medium | 76 | 96 |
| Title 2 | Medium | 57 | 66 |
| Title 3 | Medium | 48 | 56 |
| Headline | Medium | 38 | 46 |
| Subtitle 1 | Regular | 38 | 46 |
| Callout | Medium | 31 | 38 |
| Body | Medium | 29 | 36 |
| Caption 1 | Regular | 25 | 32 |
| Caption 2 | Medium | 23 | 30 |



| Style (emphasized) | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Title 1 | Bold | 76 | 96 |
| Title 2 | Bold | 57 | 66 |
| Title 3 | Bold | 48 | 56 |
| Headline | Bold | 38 | 46 |
| Subtitle 1 | Medium | 38 | 46 |
| Callout | Bold | 31 | 38 |
| Body | Bold | 29 | 36 |
| Caption 1 | Medium | 25 | 32 |
| Caption 2 | Bold | 23 | 30 |

Not all apps express tracking values as 1/1000em. Point size based on image resolution of 72 ppi for @1x and 144 ppi for @2x designs.

### [tvOS tracking values](/design/human-interface-guidelines/typography#tvOS-tracking-values)



| Size (points) | Tracking (1/1000em) | Tracking (points) |
| --- | --- | --- |
| 6 | +41 | +0.24 |
| 7 | +34 | +0.23 |
| 8 | +26 | +0.21 |
| 9 | +19 | +0.17 |
| 10 | +12 | +0.12 |
| 11 | +6 | +0.06 |
| 12 | 0 | 0.0 |
| 13 | -6 | -0.08 |
| 14 | -11 | -0.15 |
| 15 | -16 | -0.23 |
| 16 | -20 | -0.31 |
| 17 | -26 | -0.43 |
| 18 | -25 | -0.44 |
| 19 | -24 | -0.45 |
| 20 | -23 | -0.45 |
| 21 | -18 | -0.36 |
| 22 | -12 | -0.26 |
| 23 | -4 | -0.10 |
| 24 | +3 | +0.07 |
| 25 | +6 | +0.15 |
| 26 | +8 | +0.22 |
| 27 | +11 | +0.29 |
| 28 | +14 | +0.38 |
| 29 | +14 | +0.40 |
| 30 | +14 | +0.40 |
| 31 | +13 | +0.39 |
| 32 | +13 | +0.41 |
| 33 | +12 | +0.40 |
| 34 | +12 | +0.40 |
| 35 | +11 | +0.38 |
| 36 | +10 | +0.37 |
| 37 | +10 | +0.36 |
| 38 | +10 | +0.37 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.37 |
| 41 | +9 | +0.36 |
| 42 | +9 | +0.37 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.35 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +7 | +0.33 |
| 50 | +7 | +0.34 |
| 51 | +7 | +0.35 |
| 52 | +6 | +0.31 |
| 53 | +6 | +0.33 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +5 | +0.28 |
| 60 | +4 | +0.26 |
| 62 | +4 | +0.24 |
| 64 | +4 | +0.22 |
| 66 | +3 | +0.19 |
| 68 | +2 | +0.17 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.14 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0 |
| 84 | 0 | 0 |
| 88 | 0 | 0 |
| 92 | 0 | 0 |
| 96 | 0 | 0 |

Not all apps express tracking values as 1/1000em. Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs.

### [watchOS Dynamic Type sizes](/design/human-interface-guidelines/typography#watchOS-Dynamic-Type-sizes)

* [xSmall](#)
* [Small](#)
* [Large](#)
* [xLarge](#)
* [xxLarge](#)
* [xxxLarge](#)
#### [xSmall](/design/human-interface-guidelines/typography#xSmall)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 30 | 32.5 |
| Title 1 | Regular | 28 | 30.5 |
| Title 2 | Regular | 24 | 26.5 |
| Title 3 | Regular | 17 | 19.5 |
| Headline | Semibold | 14 | 16.5 |
| Body | Regular | 14 | 16.5 |
| Caption 1 | Regular | 13 | 15.5 |
| Caption 2 | Regular | 12 | 14.5 |
| Footnote 1 | Regular | 11 | 13.5 |
| Footnote 2 | Regular | 10 | 12.5 |

#### [Small (default 38mm)](/design/human-interface-guidelines/typography#Small-default-38mm)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 32 | 34.5 |
| Title 1 | Regular | 30 | 32.5 |
| Title 2 | Regular | 26 | 28.5 |
| Title 3 | Regular | 18 | 20.5 |
| Headline | Semibold | 15 | 17.5 |
| Body | Regular | 15 | 17.5 |
| Caption 1 | Regular | 14 | 16.5 |
| Caption 2 | Regular | 13 | 15.5 |
| Footnote 1 | Regular | 12 | 14.5 |
| Footnote 2 | Regular | 11 | 13.5 |

#### [Large (default 40mm/41mm/42mm)](/design/human-interface-guidelines/typography#Large-default-40mm41mm42mm)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 36 | 38.5 |
| Title 1 | Regular | 34 | 36.5 |
| Title 2 | Regular | 27 | 30.5 |
| Title 3 | Regular | 19 | 21.5 |
| Headline | Semibold | 16 | 18.5 |
| Body | Regular | 16 | 18.5 |
| Caption 1 | Regular | 15 | 17.5 |
| Caption 2 | Regular | 14 | 16.5 |
| Footnote 1 | Regular | 13 | 15.5 |
| Footnote 2 | Regular | 12 | 14.5 |

#### [xLarge (default 44mm/45mm/49mm)](/design/human-interface-guidelines/typography#xLarge-default-44mm45mm49mm)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 40 | 42.5 |
| Title 1 | Regular | 38 | 40.5 |
| Title 2 | Regular | 30 | 32.5 |
| Title 3 | Regular | 20 | 22.5 |
| Headline | Semibold | 17 | 19.5 |
| Body | Regular | 17 | 19.5 |
| Caption 1 | Regular | 16 | 18.5 |
| Caption 2 | Regular | 15 | 17.5 |
| Footnote 1 | Regular | 14 | 16.5 |
| Footnote 2 | Regular | 13 | 15.5 |

#### [xxLarge](/design/human-interface-guidelines/typography#xxLarge)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 41 | 43.5 |
| Title 1 | Regular | 39 | 41.5 |
| Title 2 | Regular | 31 | 33.5 |
| Title 3 | Regular | 21 | 23.5 |
| Headline | Semibold | 18 | 20.5 |
| Body | Regular | 18 | 20.5 |
| Caption 1 | Regular | 17 | 19.5 |
| Caption 2 | Regular | 15 | 18.5 |
| Footnote 1 | Regular | 15 | 17.5 |
| Footnote 2 | Regular | 14 | 16.5 |

#### [xxxLarge](/design/human-interface-guidelines/typography#xxxLarge)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 42 | 44.5 |
| Title 1 | Regular | 40 | 42.5 |
| Title 2 | Regular | 32 | 34.5 |
| Title 3 | Regular | 22 | 24.5 |
| Headline | Semibold | 19 | 21.5 |
| Body | Regular | 19 | 21.5 |
| Caption 1 | Regular | 18 | 20.5 |
| Caption 2 | Regular | 17 | 19.5 |
| Footnote 1 | Regular | 16 | 18.5 |
| Footnote 2 | Regular | 15 | 17.5 |

### [watchOS larger accessibility type sizes](/design/human-interface-guidelines/typography#watchOS-larger-accessibility-type-sizes)

* [AX1](#)
* [AX2](#)
* [AX3](#)
#### [AX1](/design/human-interface-guidelines/typography#AX1)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 44 | 46.5 |
| Title 1 | Regular | 42 | 44.5 |
| Title 2 | Regular | 34 | 41 |
| Title 3 | Regular | 24 | 26.5 |
| Headline | Semibold | 21 | 23.5 |
| Body | Regular | 21 | 23.5 |
| Caption 1 | Regular | 18 | 20.5 |
| Caption 2 | Regular | 17 | 19.5 |
| Footnote 1 | Regular | 16 | 18.5 |
| Footnote 2 | Regular | 15 | 17.5 |

#### [AX2](/design/human-interface-guidelines/typography#AX2)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 45 | 47.5 |
| Title 1 | Regular | 43 | 46 |
| Title 2 | Regular | 35 | 37.5 |
| Title 3 | Regular | 25 | 27.5 |
| Headline | Semibold | 22 | 24.5 |
| Body | Regular | 22 | 24.5 |
| Caption 1 | Regular | 19 | 21.5 |
| Caption 2 | Regular | 18 | 20.5 |
| Footnote 1 | Regular | 17 | 19.5 |
| Footnote 2 | Regular | 16 | 17.5 |

#### [AX3](/design/human-interface-guidelines/typography#AX3)



| Style | Weight | Size (points) | Leading (points) |
| --- | --- | --- | --- |
| Large Title | Regular | 46 | 48.5 |
| Title 1 | Regular | 44 | 47 |
| Title 2 | Regular | 36 | 38.5 |
| Title 3 | Regular | 26 | 28.5 |
| Headline | Semibold | 23 | 25.5 |
| Body | Regular | 23 | 25.5 |
| Caption 1 | Regular | 20 | 22.5 |
| Caption 2 | Regular | 19 | 21.5 |
| Footnote 1 | Regular | 18 | 20.5 |
| Footnote 2 | Regular | 17 | 19.5 |

### [watchOS tracking values](/design/human-interface-guidelines/typography#watchOS-tracking-values)

* [SF Compact](#)
* [SF Compact Rounded](#)
#### [SF Compact](/design/human-interface-guidelines/typography#SF-Compact)



| Size (points) | Tracking (1/1000em) | Tracking (points) |
| --- | --- | --- |
| 6 | +50 | +0.29 |
| 7 | +30 | +0.21 |
| 8 | +30 | +0.23 |
| 9 | +30 | +0.26 |
| 10 | +30 | +0.29 |
| 11 | +24 | +0.26 |
| 12 | +20 | +0.23 |
| 13 | +16 | +0.20 |
| 14 | +14 | +0.19 |
| 15 | +4 | +0.06 |
| 16 | 0 | 0.00 |
| 17 | -4 | -0.07 |
| 18 | -8 | -0.14 |
| 19 | -12 | -0.22 |
| 20 | 0 | 0.00 |
| 21 | -2 | -0.04 |
| 22 | -4 | -0.09 |
| 23 | -6 | -0.13 |
| 24 | -8 | -0.19 |
| 25 | -10 | -0.24 |
| 26 | -11 | -0.28 |
| 27 | -12 | -0.30 |
| 28 | -12 | -0.34 |
| 29 | -14 | -0.38 |
| 30 | -14 | -0.42 |
| 31 | -15 | -0.45 |
| 32 | -16 | -0.50 |
| 33 | -17 | -0.55 |
| 34 | -18 | -0.60 |
| 35 | -18 | -0.63 |
| 36 | -20 | -0.69 |
| 37 | -20 | -0.72 |
| 38 | -20 | -0.74 |
| 39 | -20 | -0.76 |
| 40 | -20 | -0.78 |
| 41 | -20 | -0.80 |
| 42 | -20 | -0.82 |
| 43 | -20 | -0.84 |
| 44 | -20 | -0.86 |
| 45 | -20 | -0.88 |
| 46 | -20 | -0.92 |
| 47 | -20 | -0.94 |
| 48 | -20 | -0.96 |
| 49 | -21 | -1.00 |
| 50 | -21 | -1.03 |
| 51 | -21 | -1.05 |
| 52 | -21 | -1.07 |
| 53 | -22 | -1.11 |
| 54 | -22 | -1.13 |
| 56 | -22 | -1.20 |
| 58 | -22 | -1.25 |
| 60 | -22 | -1.32 |
| 62 | -22 | -1.36 |
| 64 | -23 | -1.44 |
| 66 | -24 | -1.51 |
| 68 | -24 | -1.56 |
| 70 | -24 | -1.64 |
| 72 | -24 | -1.69 |
| 76 | -25 | -1.86 |
| 80 | -26 | -1.99 |
| 84 | -26 | -2.13 |
| 88 | -26 | -2.28 |
| 92 | -28 | -2.47 |
| 96 | -28 | -2.62 |

Not all apps express tracking values as 1/1000em. Point size based on image resolution of 144 ppi for @2x designs.

#### [SF Compact Rounded](/design/human-interface-guidelines/typography#SF-Compact-Rounded)



| Size (points) | Tracking (1/1000em) | Tracking (points) |
| --- | --- | --- |
| 6 | +28 | +0.16 |
| 7 | +26 | +0.18 |
| 8 | +24 | +0.19 |
| 9 | +22 | +0.19 |
| 10 | +20 | +0.20 |
| 11 | +18 | +0.19 |
| 12 | +16 | +0.19 |
| 13 | +14 | +0.18 |
| 14 | +12 | +0.16 |
| 15 | +10 | +0.15 |
| 16 | +8 | +0.12 |
| 17 | +6 | +0.10 |
| 18 | +4 | +0.07 |
| 19 | +2 | +0.04 |
| 20 | 0 | 0.00 |
| 21 | -2 | -0.04 |
| 22 | -4 | -0.09 |
| 23 | -6 | -0.13 |
| 24 | -8 | -0.19 |
| 25 | -10 | -0.24 |
| 26 | -11 | -0.28 |
| 27 | -12 | -0.30 |
| 28 | -12 | -0.34 |
| 29 | -14 | -0.38 |
| 30 | -14 | -0.42 |
| 31 | -15 | -0.45 |
| 32 | -16 | -0.50 |
| 33 | -17 | -0.55 |
| 34 | -18 | -0.60 |
| 35 | -18 | -0.63 |
| 36 | -20 | -0.69 |
| 37 | -20 | -0.72 |
| 38 | -20 | -0.74 |
| 39 | -20 | -0.76 |
| 40 | -20 | -0.78 |
| 41 | -20 | -0.80 |
| 42 | -20 | -0.82 |
| 43 | -20 | -0.84 |
| 44 | -20 | -0.86 |
| 45 | -20 | -0.88 |
| 46 | -20 | -0.92 |
| 47 | -20 | -0.94 |
| 48 | -20 | -0.96 |
| 49 | -21 | -1.00 |
| 50 | -21 | -1.03 |
| 51 | -21 | -1.05 |
| 52 | -21 | -1.07 |
| 53 | -22 | -1.11 |
| 54 | -22 | -1.13 |
| 56 | -22 | -1.20 |
| 58 | -22 | -1.25 |
| 60 | -22 | -1.32 |
| 62 | -22 | -1.36 |
| 64 | -23 | -1.44 |
| 66 | -24 | -1.51 |
| 68 | -24 | -1.56 |
| 70 | -24 | -1.64 |
| 72 | -24 | -1.69 |
| 76 | -25 | -1.86 |
| 80 | -26 | -1.99 |
| 84 | -26 | -2.13 |
| 88 | -26 | -2.28 |
| 92 | -28 | -2.47 |
| 96 | -28 | -2.62 |

Not all apps express tracking values as 1/1000em. Point size based on image resolution of 144 ppi for @2x designs.

[Resources](/design/human-interface-guidelines/typography#Resources)
--------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/typography#Related)

[Fonts](https://developer.apple.com/fonts/)


[SF Symbols](/design/human-interface-guidelines/sf-symbols)


#### [Developer documentation](/design/human-interface-guidelines/typography#Developer-documentation)

[`Font`](/documentation/SwiftUI/Font)


[`UIFont`](/documentation/uikit/uifont)


[`NSFont`](/documentation/appkit/nsfont)


#### [Videos](/design/human-interface-guidelines/typography#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/124/F688D32F-15D2-4082-9505-DB2FA7FE0B0B/6736_wide_250x141_1x.jpg) Meet the expanded San Francisco font family](https://developer.apple.com/videos/play/wwdc2022/110381) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/119/6436D60A-2654-4848-AC16-01C299860E5C/4951_wide_250x141_1x.jpg) Meet TextKit 2](https://developer.apple.com/videos/play/wwdc2021/10061) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/49/EA12E035-968D-4B74-AC8D-26CFD8F365A7/3823_wide_250x141_1x.jpg) The details of UI typography](https://developer.apple.com/videos/play/wwdc2020/10175) 
[Change log](/design/human-interface-guidelines/typography#Change-log)
----------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |

