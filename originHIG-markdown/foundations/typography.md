# **[foundations] typography**

### In addition to ensuring legible text, your typographic choices can help you clarify an information hierarchy, communicate important content, and express your brand.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-typography-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-typography-intro-dark_2x.png)

# **Best practices**

**Strive to maintain a minimum font size that most people can read easily.** Differences in device displays, including pixel density and brightness, can influence the appropriate minimum font size. Other factors — such as the reader’s proximity to the display, their eyesight and whether they’re in motion, and environmental lighting conditions — all impact legibility. When you support Dynamic Type — a feature that lets people choose the size of onscreen text in iOS, iPadOS, tvOS, and watchOS — your app or game can respond appropriately when people adjust text to a size that works for them. For developer guidance, see [Text input and output](https://developer.apple.com/documentation/swiftui/text-input-and-output); for available sizes, see [Specifications](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#specifications).

**Adjust font weight, size, and color as needed to emphasize important information and help people visualize hierarchy.** Be sure to maintain the relative hierarchy and visual distinction of text elements when people adjust text sizes.

**Minimize the number of typefaces you use in your interface.** Mixing too many different typefaces can obscure your information hierarchy and hinder readability.

**Test legibility in different contexts.** For example, in addition to adjusting text size, people may view your content outside in bright sunlight, glance at it while they’re in motion, or view it from a distance. If testing shows that some of your text is difficult to read, consider modifying the text or background colors to increase contrast, using a larger type size, or using typefaces designed for optimized legibility, like the system fonts.

**In general, avoid light font weights to help maintain readability.** For example, if you’re using system-provided fonts, use Regular, Medium, Semibold, or Bold font weights, and avoid Ultralight, Thin, and Light font weights, which can be difficult to see, especially when text is small.

**Prioritize important content when responding to text-size changes.** Not all content is equally important. When someone chooses a larger text size, they typically want to make the content they care about easier to read; they don’t always want to increase the size of every word on the screen. For example, when people choose a large accessibility text size, Mail displays the subject and body of the message in the large size, but leaves less important text — such as the date and the sender — in a smaller size.

# **Using system fonts**

Apple provides two typeface families that support an extensive range of weights, sizes, styles, and languages.

**San Francisco (SF)** is a sans serif typeface family that includes the SF Pro, SF Compact, SF Arabic, and SF Mono variants.

![https://developer.apple.com/design/human-interface-guidelines/foundations/typography/images/sf-pro-text-regular_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/typography/images/sf-pro-text-regular_2x.png)

The system also offers the SF Pro Rounded, SF Arabic Rounded, and SF Compact Rounded variants you can use to coordinate text with the appearance of soft or rounded UI elements, or to provide an alternative typographic voice.

**New York (NY)** is a serif typeface family designed to work well by itself and alongside the SF fonts.

![https://developer.apple.com/design/human-interface-guidelines/foundations/typography/images/new-york_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/typography/images/new-york_2x.png)

You can download the San Francisco and New York fonts [here](https://developer.apple.com/fonts/).

The system provides the SF and NY fonts in the *variable* font format, which combines different font styles together in one file, and supports interpolation between styles to create intermediate ones.

**NOTE**Variable fonts enable *optical sizing*, which refers to the adjustment of different typographic designs to fit different sizes. On all platforms, the system fonts support *dynamic optical sizes*, which merge discrete optical sizes (like Text and Display) and weights into a single, continuous design, letting the system interpolate each glyph or letterform to produce a structure that’s precisely adapted to the point size. With dynamic optical sizes, you don’t need to use discrete optical sizes unless you’re working with a design tool that doesn’t support all the features of the variable font format.

To help you define visual hierarchies and create clear and legible designs in many different sizes and contexts, the system fonts are available in a variety of weights, ranging from Ultralight to Black, and — in the case of SF — several widths, including Condensed and Expanded. Because SF Symbols use equivalent weights, you can achieve precise weight matching between symbols and adjacent text, regardless of the size or style you choose.

**NOTE**[SF Symbols](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols) provides a comprehensive library of symbols that integrate seamlessly with the San Francisco system font, automatically aligning with text in all weights and sizes. Consider using symbols when you need to convey a concept or depict an object, especially within text.

The system defines a set of typographic attributes — called text styles — that work with both typeface families. A *text style* specifies a combination of font weight, point size, and leading values for each text size. For example, the *body* text style uses values that support a comfortable reading experience over multiple lines of text, while the *headline* style assigns a font size and weight that help distinguish a heading from surrounding content. Taken together, the text styles form a typographic hierarchy you can use to express the different levels of importance in your content. Text styles also allow text to scale proportionately when people change the system’s text size or make accessibility adjustments, like turning on Larger Text in Accessibility settings.

**Consider using the built-in text styles.** The system-defined text styles give you a convenient and consistent way to convey your information hierarchy through font size and weight. Using text styles with the system fonts also supports Dynamic Type and the larger accessibility type sizes (where available), which let people choose the text size that works for them.

**Modify the built-in text styles if necessary.** System APIs define font adjustments — called *symbolic traits* — that let you modify some aspects of a text style. For example, the bold trait adds weight to text, letting you create another level of hierarchy. You can also use symbolic traits to adjust leading if you need to improve readability or conserve space. For example, when you display text in wide columns or long passages, more space between lines (*loose leading*) can make it easier for people to keep their place while moving from one line to the next. Conversely, if you need to display multiple lines of text in an area where height is constrained — for example, in a list row — decreasing the space between lines (*tight leading*) can help the text fit well. If you need to display three or more lines of text, avoid tight leading even in areas where height is limited. For developer guidance, see [leading(_:)](https://developer.apple.com/documentation/swiftui/font/leading(_:)).

**Adjust tracking as needed in interface mockups.** In a running app, the system font dynamically adjusts tracking at every point size. To produce an accurate interface mockup of an interface that uses the variable system fonts, you don’t have to choose a discrete optical size at certain point sizes, but you might need to adjust the tracking. For guidance, see [Specifications](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#specifications).

**DEVELOPER NOTE**You can use the constants defined in [Font.Design](https://developer.apple.com/documentation/swiftui/font/design) to access all system fonts — don’t embed system fonts in your app or game. For example, use [default](https://developer.apple.com/documentation/swiftui/font/design/default) to get the system font on all platforms; use [serif](https://developer.apple.com/documentation/swiftui/font/design/serif) to get the New York font.

# **Using custom fonts**

**Make sure custom fonts are legible.** Unless your app has a compelling need for a custom font — such as for branding purposes or to create an immersive gaming experience — prefer the system fonts. If you do use a custom font, make sure people can read it easily at various viewing distances and under a variety of conditions.

**Implement accessibility features for custom fonts.** System fonts automatically support Dynamic Type (where available) and respond when people turn on accessibility features, such as Bold Text. If you use a custom font, make sure it implements the same behaviors. For developer guidance, see [Applying custom fonts to text](https://developer.apple.com/documentation/swiftui/applying-custom-fonts-to-text).

# **Platform considerations**

# **iOS, iPadOS**

SF Pro is the system font in iOS and iPadOS. iOS and iPadOS apps can also use NY.

# **macOS**

SF Pro is the system font in macOS. NY is available for Mac apps built with Mac Catalyst. macOS doesn’t support Dynamic Type.

**When necessary, use dynamic system font variants to match the text in standard controls.** Dynamic system font variants give your text the same look and feel of the text that appears in system-provided controls. Use the variants listed below to achieve a look that’s consistent with other apps on the platform.

# **tvOS**

SF Pro is the system font in tvOS, and apps can also use NY.

# **watchOS**

SF Compact is the system font in watchOS, and apps can also use NY. In complications, watchOS uses SF Compact Rounded.

# **Specifications**

# **iOS, iPadOS**

### **Dynamic Type sizes (iOS)**

• [xSmall](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [Small](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [Medium](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [Large (Default)](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [xLarge](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [xxLarge](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [xxxLarge](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)

- **Large (Default)**
    
    Point size based on image resolution of 144ppi for @2x and 216ppi for @3x designs.
    

### **Larger accessibility type sizes (iOS)**

• [AX1](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [AX2](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [AX3](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [AX4](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [AX5](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)

- **AX1**
    
    Point size based on image resolution of 144ppi for @2x and 216ppi for @3x designs.
    

### **Tracking values (iOS)**

• [SF Pro](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [SF Pro Rounded](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [New York](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)

- **SF Pro**
    
    Not all apps express tracking values as 1/1000em. Point size based on image resolution of 144ppi for @2x and 216ppi for @3x designs.
    

# **macOS**

### **Built-in text styles**

Point size based on image resolution of 144ppi for @2x designs.

### **Tracking values (macOS)**

Not all apps express tracking values as 1/1000em. Point size based on image resolution of 144ppi for @2x and 216ppi for @3x designs.

# **tvOS**

### **Dynamic Type sizes (tvOS)**

Not all apps express tracking values as 1/1000em. Point size based on image resolution of 72ppi for @1x and 144ppi for @2x designs.

### **Tracking values (tvOS)**

Not all apps express tracking values as 1/1000em. Point size based on image resolution of 144ppi for @2x and 216ppi for @3x designs.

# **watchOS**

### **Dynamic Type sizes (watchOS)**

• [xSmall](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [Small](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [Large](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [xLarge](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [xxLarge](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [xxxLarge](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)

- **Large (default 40mm/41mm/42mm)**

### **Larger accessibility type sizes (watchOS)**

• [AX1](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [AX2](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [AX3](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)

- **AX1**

### **Tracking values (watchOS)**

• [SF Compact](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)
• [SF Compact Rounded](https://developer.apple.com/design/human-interface-guidelines/foundations/typography#)

- **SF Compact**
    
    Not all apps express tracking values as 1/1000em. Point size based on image resolution of 144ppi for @2x designs.
    

| Dynamic font variant | API |
| --- | --- |
| Control content | controlContentFontOfSize |
| Label | labelFontOfSize |
| Menu | menuFontOfSize |
| Menu bar | menuBarFontOfSize |
| Message | messageFontOfSize |
| Palette | paletteFontOfSize |
| Title | titleBarFontOfSize |
| Tool tips | toolTipsFontOfSize |
| Document text (user) | userFontOfSize |
| Monospaced document text (user fixed pitch) | userFixedPitchFontOfSize |
| Bold system font | boldSystemFontOfSize |
| System font | systemFontOfSize |

| Text style | Weight | Size (points) | Line height (points) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 26 | 32 | Bold |
| Title 1 | Regular | 22 | 26 | Bold |
| Title 2 | Regular | 17 | 22 | Bold |
| Title 3 | Regular | 15 | 20 | Semibold |
| Headline | Bold | 13 | 16 | Heavy |
| Subheadline | Regular | 11 | 14 | Semibold |
| Body | Regular | 13 | 16 | Semibold |
| Callout | Regular | 12 | 15 | Semibold |
| Footnote | Regular | 10 | 13 | Semibold |
| Caption 1 | Regular | 10 | 13 | Medium |
| Caption 2 | Medium | 10 | 13 | Semibold |

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
| Title 1 | Bold | 76 | 96 | +11 |
| Title 2 | Bold | 57 | 66 | +13 |
| Title 3 | Bold | 48 | 56 | +15 |
| Headline | Bold | 38 | 46 | -26 |
| Subtitle 1 | Medium | 38 | 46 | -26 |
| Callout | Bold | 31 | 38 | -16 |
| Body | Bold | 29 | 36 | -13 |
| Caption 1 | Medium | 25 | 32 | -3 |
| Caption 2 | Bold | 23 | 30 | +3 |

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