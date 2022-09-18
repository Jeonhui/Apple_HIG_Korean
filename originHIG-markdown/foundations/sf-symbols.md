# **[foundations] sf-symbols**

### SF Symbols provides thousands of consistent, highly configurable symbols that integrate seamlessly with the San Francisco system font, automatically aligning with text in all weights and sizes.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-sf-symbols-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-sf-symbols-intro-dark_2x.png)

You can use a symbol to convey an object or concept wherever interface icons can appear, such as in navigation bars, toolbars, tab bars, context menus, and within text.

Availability of individual symbols and features varies based on the version of the system you’re targeting. For example, if you add to your app bundle a symbol introduced in SF Symbols 3, you can use the symbol when your app runs in earlier platforms — such as iOS 13, Mac Catalyst 13, tvOS 13, or watchOS 6 — but without the benefit of SF Symbols 3 features like Hierarchical or Palette color rendering.

Visit [SF Symbols](https://developer.apple.com/sf-symbols/) to download the app and browse the full set of symbols. Be sure to understand the terms and conditions for using SF Symbols, including the prohibition against using symbols — or images that are confusingly similar — in app icons, logos, or any other trademarked use. For developer guidance, see [Configuring and displaying symbol images in your UI](https://developer.apple.com/documentation/uikit/uiimage/configuring_and_displaying_symbol_images_in_your_ui/).

# **Rendering modes**

SF Symbols 3 and later provide four rendering modes — monochrome, hierarchical, palette, and multicolor — that enable multiple options when applying color to symbols. For example, you might want to use multiple opacities of your app’s accent color to give symbols depth and emphasis, or specify a palette of contrasting colors to display symbols that coordinate with various color schemes.

To support the rendering modes, SF Symbols organizes a symbol’s paths into distinct layers. For example, the `cloud.sun.rain.fill` symbol consists of three layers: the primary layer contains the cloud paths, the secondary layer contains the paths that define the sun and its rays, and the tertiary layer contains the raindrop paths.

![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/three-layers-primary-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/three-layers-primary-dark_2x.png)

Primary

![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/three-layers-secondary-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/three-layers-secondary-dark_2x.png)

Secondary

![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/three-layers-tertiary-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/three-layers-tertiary-dark_2x.png)

Tertiary

Depending on the rendering mode you choose, a symbol can produce various appearances. For example, Hierarchical rendering mode assigns a different opacity of a single color to each layer, creating a visual hierarchy that gives depth to the symbol.

![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/three-layers-color-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/three-layers-color-dark_2x.png)

To learn more about supporting rendering modes in custom symbols, see [Custom symbols](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols#custom-symbols).

SF Symbols supports the following rendering modes.

**Monochrome** — Applies one color to all layers in a symbol. Within a symbol, paths render in the color you specify or as a transparent shape within a color-filled path.

![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/monochrome-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/monochrome-dark_2x.png)

**Hierarchical** — Applies one color to all layers in a symbol, varying the color’s opacity according to each layer’s hierarchical level.

![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/hierarchical-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/hierarchical-dark_2x.png)

**Palette** — Applies two or more colors to a symbol, using one color per layer. Specifying only two colors for a symbol that defines three levels of hierarchy means the secondary and tertiary layers use the same color.

![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/palette-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/palette-dark_2x.png)

**Multicolor** — Applies intrinsic colors to some symbols to enhance meaning. For example, the `leaf` symbol uses green to reflect the appearance of leaves in the physical world, whereas the `trash.slash` symbol uses red to signal data loss. Some multicolor symbols include layers that can receive other colors.

![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/multicolor-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/multicolor-dark_2x.png)

Regardless of rendering mode, using system-provided colors ensures that symbols automatically adapt to accessibility accommodations and appearance modes like vibrancy and Dark Mode. For developer guidance, see [renderingMode(_:)](https://developer.apple.com/documentation/swiftui/image/renderingmode(_:)).

**Confirm that a symbol’s rendering mode works well in every context.** Depending on factors like the size of a symbol and its contrast with the current background color, different rendering modes can affect how well people can discern the symbol’s details. In SF Symbols 4 and later, you can use the automatic setting to get a symbol’s preferred rendering mode, but it’s still a good idea to check the results for places where a different rendering mode might improve a symbol’s legibility.

# **Variable color**

With variable color, SF Symbols 4 introduces a way to represent a characteristic that can change over time — like capacity or strength — regardless of rendering mode. To visually communicate such a change, variable color applies color to different layers of a symbol as a value reaches different thresholds between zero and 100 percent.

For example, you could use variable color with the `speaker.wave.3` symbol to communicate three different ranges of sound — plus the state where there’s no sound — by mapping the layers that represent the curved wave paths to different ranges of decibel values. In the case of no sound, no wave layers get color. In all other cases, a wave layer receives color when the sound reaches a threshold the system defines based on the number of nonzero states you want to represent.

![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/variable-color_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/variable-color_2x.png)

Sometimes, it can make sense for some of a symbol’s layers to opt out of variable color. For example, in the `speaker.wave.3` symbol shown above, the layer that contains the speaker path doesn’t receive variable color because a speaker doesn’t change as the sound level changes. A symbol can support variable color in any number of layers.

**Use variable color to communicate change — don’t use it to communicate depth.** To convey depth and visual hierarchy, use Hierarchical rendering mode to elevate certain layers and distinguish foreground and background elements in a symbol.

# **Weights and scales**

SF Symbols provides symbols in a wide range of weights and scales to help you create adaptable designs.

![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/scales-weights-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/scales-weights-dark_2x.png)

Each of the nine symbol weights — from ultralight to black — corresponds to a weight of the San Francisco system font, helping you achieve precise weight matching between symbols and adjacent text, while supporting flexibility for different sizes and contexts.

Each symbol is also available in three scales: small, medium (the default), and large. The scales are defined relative to the cap height of the San Francisco system font.

![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/small-medium-large-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/small-medium-large-dark_2x.png)

Specifying a scale lets you adjust a symbol’s emphasis compared to adjacent text, without disrupting the weight matching with text that uses the same point size. For developer guidance, see [imageScale](https://developer.apple.com/documentation/swiftui/view/3280160-imagescale) (SwiftUI), [SymbolScale](https://developer.apple.com/documentation/uikit/uiimage/symbolscale) (UIKit), and [SymbolConfiguration](https://developer.apple.com/documentation/appkit/nsimage/symbolconfiguration) (AppKit).

# **Design variants**

SF Symbols defines several design variants — such as fill, slash, and enclosed — that can help you communicate precise states and actions while maintaining visual consistency and simplicity in your UI. For example, you could use the slash variant of a symbol to show that an item or action is unavailable, or use the fill variant to indicate selection.

Outline is the most common variant in SF Symbols. An outlined symbol has no solid areas, resembling the appearance of text. Most symbols are also available in a fill variant, in which the areas within some shapes are solid.

In addition to outline and fill, SF Symbols also defines variants that include a slash or enclose a symbol within a shape like a circle, square, or rectangle. In many cases, enclosed and slash variants can combine with outline or fill variants.

![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/variants-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/variants-dark_2x.png)

SF Symbols 3 and later provides many variants for specific languages and writing systems, including Latin, Arabic, Hebrew, Hindi, Thai, Chinese, Japanese, and Korean. Language- and script-specific variants adapt automatically when the device language changes. For guidance, see [Images](https://developer.apple.com/design/human-interface-guidelines/foundations/right-to-left/#images).

![https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/localized-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/images/localized-dark_2x.png)

Symbol variants support a range of design goals. For example:

- The outline variant works well in toolbars, navigation bars, lists, and other places where you display a symbol alongside text.
- Symbols that use an enclosing shape — like a square or circle — can improve legibility at small sizes.
- The solid areas in a fill variant tend to give a symbol more visual emphasis, making it a good choice for iOS tab bars and swipe actions and places where you use an accent color to communicate selection.

In many cases, the view that displays a symbol determines whether to use outline or fill, so you don’t have to specify a variant. For example, an iOS tab bar prefers the fill variant, whereas a navigation bar takes the outline variant.

# **Custom symbols**

If you need a symbol that SF Symbols doesn’t provide, you can create your own. To create a custom symbol, first export the template for a symbol that’s similar to the design you want, then use a vector-editing tool like Sketch or Illustrator to modify it. For developer guidance, see [Creating custom symbol images for your app](https://developer.apple.com/documentation/uikit/uiimage/creating_custom_symbol_images_for_your_app/).

**IMPORTANT**SF Symbols includes copyrighted symbols that depict Apple products and features. You can display these symbols in your app, but you can’t customize them. To help you identify a noncustomizable symbol, the SF Symbols app badges it with an Info icon; to help you use the symbol correctly, the inspector pane describes its usage restrictions.

Using a process called *annotating*, you can assign a specific color — or a specific hierarchical level, such as primary, secondary, or tertiary — to each layer in a custom symbol. Depending on the rendering modes you support, you can use a different mode in each instance of the symbol in your app.

**Use the template as a guide.** Create a custom symbol that’s consistent with the ones the system provides in level of detail, optical weight, alignment, position, and perspective. Strive to design a symbol that is:

- Simple
- Recognizable
- Inclusive
- Directly related to the action or content it represents

For guidance, see [Icons](https://developer.apple.com/design/human-interface-guidelines/foundations/icons).

**Assign negative side margins to your custom symbol if necessary.** SF Symbols supports negative side margins to aid optical horizontal alignment when a symbol contains a badge or other elements that increase its width. For example, negative side margins can help you horizontally align a stack of folder symbols, some of which include a badge. Beginning in SF Symbols 3, the name of each margin includes the relevant configuration — such as “left-margin-Regular-M” — so be sure to use this naming pattern if you add margins to your custom symbols.

**Provide alternative text labels for custom symbols.** Alternative text labels — or accessibility descriptions — aren’t visible, but they let VoiceOver describe what’s on screen, making navigation easier for people with visual disabilities. For guidance, see [VoiceOver](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility/#voiceover).

**Don’t design replicas of Apple products.** Apple products are copyrighted and you can’t reproduce them in your custom symbols. Also, you can’t customize a symbol that SF Symbols identifies as representing an Apple feature or product.

# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.*