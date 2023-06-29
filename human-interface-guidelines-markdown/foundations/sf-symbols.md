June 5, 2023

 Added a new section on animations. Included animation guidance for custom symbols. SF Symbols
==========

SF Symbols provides thousands of consistent, highly configurable symbols that integrate seamlessly with the San Francisco system font, automatically aligning with text in all weights and sizes.![A sketch of the SF Symbols icon. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/06d528652b87b23f1cecaf5faceedf30/foundations-sf-symbols-intro@2x.png)

You can use a symbol to convey an object or concept wherever interface icons can appear, such as in navigation bars, toolbars, tab bars, context menus, and within text.

Availability of individual symbols and features varies based on the version of the system you’re targeting. Symbols and symbol features introduced in a given year aren’t available in earlier operating systems.

Visit [SF Symbols](https://developer.apple.com/sf-symbols/)
 to download the app and browse the full set of symbols. Be sure to understand the terms and conditions for using SF Symbols, including the prohibition against using symbols — or images that are confusingly similar — in app icons, logos, or any other trademarked use. For developer guidance, see [Configuring and displaying symbol images in your UI](/documentation/uikit/uiimage/configuring_and_displaying_symbol_images_in_your_ui)
.

[Rendering modes](/design/human-interface-guidelines/sf-symbols#Rendering-modes)
--------------------------------------------------------------------------------

SF Symbols 3 and later provide four rendering modes — monochrome, hierarchical, palette, and multicolor — that give you multiple options when applying color to symbols. For example, you might want to use multiple opacities of your app’s accent color to give symbols depth and emphasis, or specify a palette of contrasting colors to display symbols that coordinate with various color schemes.

To support the rendering modes, SF Symbols organizes a symbol’s paths into distinct layers. For example, the `cloud.sun.rain.fill` symbol consists of three layers: the primary layer contains the cloud paths, the secondary layer contains the paths that define the sun and its rays, and the tertiary layer contains the raindrop paths.

![An image of the cloud sun rain fill symbol. The cloud is black and the raindrops and sun are gray to indicate that the cloud is in the primary layer.](https://docs-assets.developer.apple.com/published/42c350caa5e5117d40d45ac28c258832/sf-three-layers-primary@2x.png)Primary![An image of the cloud sun rain fill symbol. The sun is black and the raindrops and cloud are gray to indicate that the sun is in the secondary layer.](https://docs-assets.developer.apple.com/published/9acc461ef73c512ab21e4713fcdc75a3/sf-three-layers-secondary@2x.png)Secondary![An image of the cloud sun rain fill symbol. The raindrops are black and the sun and cloud are gray to indicate that the raindrops are in the primary layer.](https://docs-assets.developer.apple.com/published/f2ec783b9aedc7f59c3485efb83fbb94/sf-three-layers-tertiary@2x.png)TertiaryDepending on the rendering mode you choose, a symbol can produce various appearances. For example, Hierarchical rendering mode assigns a different opacity of a single color to each layer, creating a visual hierarchy that gives depth to the symbol.

![An image of the cloud sun rain fill symbol that uses three different opacities of the system blue color in the symbol’s three different layers: the cloud is fully opaque, the sun is about 50% opaque, and the raindrops are about 25% opaque.](https://docs-assets.developer.apple.com/published/35fe9f56dee989f094845e640951fef5/sf-three-layers-color@2x.png)

To learn more about supporting rendering modes in custom symbols, see [Custom symbols](/design/human-interface-guidelines/sf-symbols#Custom-symbols)
.

SF Symbols supports the following rendering modes.

**Monochrome** — Applies one color to all layers in a symbol. Within a symbol, paths render in the color you specify or as a transparent shape within a color-filled path.

![A diagram showing a row of eight symbols, all of which use a single opacity of the system blue color.](https://docs-assets.developer.apple.com/published/b296a9ee1b06b49c011209c83b537096/sf-monochrome@2x.png)

**Hierarchical** — Applies one color to all layers in a symbol, varying the color’s opacity according to each layer’s hierarchical level.

![A diagram showing a row of eight symbols, each of which uses different opacities of the system blue color. From the left, the square and arrow up symbol uses full opacity for the arrow and low opacity in the square. Next, folder badge plus uses full opacity for the badge and low opacity for the folder. Trash slash uses full opacity for the slash and low opacity for the can. Calendar day timeline right uses full opacity for the horizontal indicator and low opacity for the square and dots. List number uses full opacity for the column of numbers and low opacity for the horizontal lines. Text format A B C dotted underline uses full opacity for the dots under the low-opacity letters. iPhone radio waves left and right uses full opacity for the device outline, mid opacity in the screen area, and low opacity for the radio wave lines. Lastly, the PC symbol uses full opacity for the device outline and the onscreen sad face and horizontal lines and mid opacity in the screen background.](https://docs-assets.developer.apple.com/published/c035476f6266b094b051d4e392329092/sf-hierarchical@2x.png)

**Palette** — Applies two or more colors to a symbol, using one color per layer. Specifying only two colors for a symbol that defines three levels of hierarchy means the secondary and tertiary layers use the same color.

![A diagram showing a row of eight symbols, each of which uses a combination of gray and the system blue color. From the left, the square and arrow up symbol uses blue for the arrow and light gray for the square. Next, folder badge plus uses blue for the badge and light gray for the folder. Trash slash uses blue for the slash and light gray for the can. Calendar day timeline right uses blue for the horizontal indicator and light gray for the square and dots. List number uses blue for the column of numbers and light gray for the horizontal lines. Text format A B C dotted underline uses blue for the dots under the light gray letters. iPhone radio waves left and right uses blue for the device outline, medium gray in the screen area, and light gray for the radio wave lines. Lastly, the PC symbol uses blue for the device outline and the onscreen sad face and horizontal lines and medium gray in the screen background.](https://docs-assets.developer.apple.com/published/5ea6a976464ec36e5dbdbf30588a25e0/sf-palette@2x.png)

**Multicolor** — Applies intrinsic colors to some symbols to enhance meaning. For example, the `leaf` symbol uses green to reflect the appearance of leaves in the physical world, whereas the `trash.slash` symbol uses red to signal data loss. Some multicolor symbols include layers that can receive other colors.

![A diagram showing a row of eight symbols, using combinations of various colors. From the left, the square and arrow up symbol uses blue for all lines. Next, folder badge plus uses green for the badge and blue for the folder. Trash slash uses red for both the slash and the can. Calendar day timeline right uses red for the horizontal indicator, dark gray for the square, and light gray for the dots. List number uses black for the column of numbers and medium gray for the horizontal lines. Text format A B C dotted underline uses red for the dots under the black letters. iPhone radio waves left and right uses blue for all lines. Lastly, the PC symbol uses yellow for the device outline, white for the onscreen sad face and horizontal lines, and blue in the screen background.](https://docs-assets.developer.apple.com/published/82097ab3d98f098d12935ab4d6c1c896/sf-multicolor@2x.png)

Regardless of rendering mode, using system-provided colors ensures that symbols automatically adapt to accessibility accommodations and appearance modes like vibrancy and Dark Mode. For developer guidance, see [renderingMode(\_:)](https://developer.apple.com/documentation/swiftui/image/renderingmode(_:))
.

**Confirm that a symbol’s rendering mode works well in every context.** Depending on factors like the size of a symbol and its contrast with the current background color, different rendering modes can affect how well people can discern the symbol’s details. In SF Symbols 4 and later, you can use the automatic setting to get a symbol’s preferred rendering mode, but it’s still a good idea to check the results for places where a different rendering mode might improve a symbol’s legibility.

[Variable color](/design/human-interface-guidelines/sf-symbols#Variable-color)
------------------------------------------------------------------------------

With variable color, SF Symbols 4 introduces a way to represent a characteristic that can change over time — like capacity or strength — regardless of rendering mode. To visually communicate such a change, variable color applies color to different layers of a symbol as a value reaches different thresholds between zero and 100 percent.

For example, you could use variable color with the `speaker.wave.3` symbol to communicate three different ranges of sound — plus the state where there’s no sound — by mapping the layers that represent the curved wave paths to different ranges of decibel values. In the case of no sound, no wave layers get color. In all other cases, a wave layer receives color when the sound reaches a threshold the system defines based on the number of nonzero states you want to represent.

![A diagram showing four versions of the speaker wave three symbol, each of which displays color in a different number of wave paths. From the left, the number of waves with color is zero, one, two, and three.](https://docs-assets.developer.apple.com/published/e03af602ef484d26ff5cc3428e98079a/sf-variable-color@2x.png)

Sometimes, it can make sense for some of a symbol’s layers to opt out of variable color. For example, in the `speaker.wave.3` symbol shown above, the layer that contains the speaker path doesn’t receive variable color because a speaker doesn’t change as the sound level changes. A symbol can support variable color in any number of layers.

**Use variable color to communicate change — don’t use it to communicate depth.** To convey depth and visual hierarchy, use Hierarchical rendering mode to elevate certain layers and distinguish foreground and background elements in a symbol.

[Weights and scales](/design/human-interface-guidelines/sf-symbols#Weights-and-scales)
--------------------------------------------------------------------------------------

SF Symbols provides symbols in a wide range of weights and scales to help you create adaptable designs.

![A diagram showing the square and arrow up symbol in all 27 weights and scales.](https://docs-assets.developer.apple.com/published/a46e2c294c605c4f5e5f626c67d6bb2d/sf-scales-weights@2x.png)

Each of the nine symbol weights — from ultralight to black — corresponds to a weight of the San Francisco system font, helping you achieve precise weight matching between symbols and adjacent text, while supporting flexibility for different sizes and contexts.

Each symbol is also available in three scales: small, medium (the default), and large. The scales are defined relative to the cap height of the San Francisco system font.

![A diagram showing the first of three images of the plus circle symbol followed by the capitalized word add. In each image, the word uses the same size, but the symbol uses a different size. The symbol size is small in this image. Two parallel horizontal lines appear across all three images. The top line shows the height of the capital letter A and the bottom line is the baseline under the word add. In this small symbol, the circle touches both lines.](https://docs-assets.developer.apple.com/published/bf6a6d81c531a772bbe9c768af32f0b8/sf-symbol-scale-small@2x.png)Small![The second of three images of the plus circle symbol followed by the capitalized word add. In this medium symbol, the circle extends slightly above and below the lines.](https://docs-assets.developer.apple.com/published/aa672f59358a8bb354e4ea9e7d258467/sf-symbol-scale-medium@2x.png)Medium![The third of three images of the plus circle symbol followed by the capitalized word add. In this large symbol, the vertical line of the plus sign almost touches both lines.](https://docs-assets.developer.apple.com/published/6696a9dbf59f8ef7118ac712067de2e6/sf-symbol-scale-large@2x.png)LargeSpecifying a scale lets you adjust a symbol’s emphasis compared to adjacent text, without disrupting the weight matching with text that uses the same point size. For developer guidance, see [`imageScale(_:)`](/documentation/SwiftUI/View/imageScale(_:))
 (SwiftUI), [`UIImage.SymbolScale`](/documentation/uikit/uiimage/symbolscale)
 (UIKit), and [`NSImage.SymbolConfiguration`](/documentation/appkit/nsimage/symbolconfiguration)
 (AppKit).

[Design variants](/design/human-interface-guidelines/sf-symbols#Design-variants)
--------------------------------------------------------------------------------

SF Symbols defines several design variants — such as fill, slash, and enclosed — that can help you communicate precise states and actions while maintaining visual consistency and simplicity in your UI. For example, you could use the slash variant of a symbol to show that an item or action is unavailable, or use the fill variant to indicate selection.

Outline is the most common variant in SF Symbols. An outlined symbol has no solid areas, resembling the appearance of text. Most symbols are also available in a fill variant, in which the areas within some shapes are solid.

In addition to outline and fill, SF Symbols also defines variants that include a slash or enclose a symbol within a shape like a circle, square, or rectangle. In many cases, enclosed and slash variants can combine with outline or fill variants.

![A diagram showing two rows of the same five symbols. In the top row, every symbol uses the outline variant; the bottom row shows the fill variant of each symbol. From the left, the symbols are heart, heart slash, heart circle, heart square, and a heart in a rectangle.](https://docs-assets.developer.apple.com/published/c4486c6d1dc36ea164665276e912139a/sf-variants@2x.png)

SF Symbols 3 and later provides many variants for specific languages and writing systems, including Latin, Arabic, Hebrew, Hindi, Thai, Chinese, Japanese, and Korean. Language- and script-specific variants adapt automatically when the device language changes. For guidance, see [Images](/design/human-interface-guidelines/right-to-left#Images)
.

![A diagram with eight rows of the same twelve symbols, where each row shows a localized version of the symbol. From the left the symbols are doc rich text, doc rich text fill, character book closed, character book closed fill, character bubble, character bubble fill, character, text format superscript, text format subscript, text format size, character text box, and character cursor I beam.](https://docs-assets.developer.apple.com/published/cf9d526c8f3a39b600f0226125a2b228/sf-localized@2x.png)

Symbol variants support a range of design goals. For example:

* The outline variant works well in toolbars, navigation bars, lists, and other places where you display a symbol alongside text.
* Symbols that use an enclosing shape — like a square or circle — can improve legibility at small sizes.
* The solid areas in a fill variant tend to give a symbol more visual emphasis, making it a good choice for iOS tab bars and swipe actions and places where you use an accent color to communicate selection.

In many cases, the view that displays a symbol determines whether to use outline or fill, so you don’t have to specify a variant. For example, an iOS tab bar prefers the fill variant, whereas a navigation bar takes the outline variant.

[Animations](/design/human-interface-guidelines/sf-symbols#Animations)
----------------------------------------------------------------------

SF Symbols provides a collection of expressive, configurable animations that enhance your interface and add vitality to your app. Symbol animations help communicate ideas, provide feedback in response to people’s actions, and signal changes in status or ongoing activities.

Animations work on all SF Symbols in the library, in all rendering modes, weights, and scales, and on custom symbols. For considerations when animating custom symbols, see [Custom symbols](/design/human-interface-guidelines/sf-symbols#Custom-symbols)
. You can control the playback of an animation, whether you want the animation to run from start to finish, or run indefinitely, repeating its effect until a condition is met. You can customize behaviors, like changing the playback speed of an animation or determining whether to reverse an animation before repeating it. For developer guidance, see [Symbols](/documentation/symbols)
 and [`SymbolEffect`](/documentation/symbols/symboleffect)
.

SF Symbols 5 and later supports the following animations.

**Appear** — Causes a symbol to gradually emerge into view.

 [Play](#) 
**Disappear** — Causes a symbol to gradually recede out of view.

 [Play](#) 
**Bounce** — Briefly scales a symbol with an elastic-like movement and then returns the symbol to its initial state. Bounce can be configured to bounce up or down. This animation plays once by default and can help communicate that an action occurred or needs to take place.

 [Play](#) 
**Scale** — Changes the size of a symbol, increasing or decreasing its scale. This effect is similar to the bounce animation but is stateful: the scaled state persists until a new scale is set or the effect is removed. You can use the scale animation to highlight a symbol, providing focus when an item is selected or as feedback when a symbol is tapped or clicked.

 [Play](#) 
**Pulse** — Varies the opacity of a symbol over time. This animation automatically pulses only the layers within a symbol that are annotated to pulse, and optionally can pulse all layers within a symbol. You can use the pulse animation to communicate ongoing activity, playing continuously until a condition is met.

 [Play](#) 
**Variable color** — Incrementally varies the opacity of layers within a symbol. This animation can be cumulative or iterative. When cumulative, color changes persist for each layer until the animation cycle is complete. When iterative, color changes occur one layer at a time. You can use variable color to communicate progress or ongoing activity, such as playback, connecting, or broadcasting. You can customize the animation to autoreverse — meaning reverse the animation to the starting point and replay the sequence — as well as hide inactive layers rather than reduce their opacity.

 [Play](#) 
**Replace** — Replaces one symbol with another. The replace animation works between arbitrary symbols and across all weights and rendering modes. This animation features three configurations:

* Down-up, where the outgoing symbol scales down and the incoming symbol scales up, communicating a change in state.
* Up-up, where both the outgoing and incoming symbols scale up. This configuration communicates a change in state that includes a sense of forward progression.
* Off-up, where the outgoing symbol hides immediately and the incoming symbol scales up. This configuration communicates a state change that emphasizes the next available state or action.

 [Play](#) 
From left to right: down-up, up-up, off-up**Apply symbol animations judiciously.** While there’s no limit to how many animations you can add to a view, too many animations can overwhelm an interface and dilute its focus or functionality.

**Make sure that animations serve a clear purpose in communicating a symbol’s intent.** Each type of animation has a discrete movement that communicates a certain type of action or elicits a certain response. Consider how people might interpret an animated symbol and whether the animation, or combination of animations, might be confusing.

**Use symbol animations to communicate information more efficiently.** Animations provide visual feedback, reinforcing that something happened in your interface. You can use animations to present complex information in a simple way and without taking up a lot of visual space.

**Consider your app’s tone when adding animations.** When animating a symbol, think about what the animation can convey and how that might align with your brand identity and your app’s overall style and tone. For guidance, see [Branding](/design/human-interface-guidelines/branding)
.

[Custom symbols](/design/human-interface-guidelines/sf-symbols#Custom-symbols)
------------------------------------------------------------------------------

If you need a symbol that SF Symbols doesn’t provide, you can create your own. To create a custom symbol, first export the template for a symbol that’s similar to the design you want, then use a vector-editing tool to modify it. For developer guidance, see [Creating custom symbol images for your app](/documentation/uikit/uiimage/creating_custom_symbol_images_for_your_app)
.

Important

SF Symbols includes copyrighted symbols that depict Apple products and features. You can display these symbols in your app, but you can’t customize them. To help you identify a noncustomizable symbol, the SF Symbols app badges it with an Info icon; to help you use the symbol correctly, the inspector pane describes its usage restrictions.

Using a process called *annotating*, you can assign a specific color — or a specific hierarchical level, such as primary, secondary, or tertiary — to each layer in a custom symbol. Depending on the rendering modes you support, you can use a different mode in each instance of the symbol in your app.

**Use the template as a guide.** Create a custom symbol that’s consistent with the ones the system provides in level of detail, optical weight, alignment, position, and perspective. Strive to design a symbol that is:

* Simple
* Recognizable
* Inclusive
* Directly related to the action or content it represents

For guidance, see [Icons](/design/human-interface-guidelines/icons)
.

**Assign negative side margins to your custom symbol if necessary.** SF Symbols supports negative side margins to aid optical horizontal alignment when a symbol contains a badge or other elements that increase its width. For example, negative side margins can help you horizontally align a stack of folder symbols, some of which include a badge. Beginning in SF Symbols 3, the name of each margin includes the relevant configuration — such as “left-margin-Regular-M” — so be sure to use this naming pattern if you add margins to your custom symbols.

**Optimize layers to use animations with custom symbols.** If you want to animate your symbol by layer, make sure to annotate the layers in the SF Symbols app. The Z-order determines the order that you want to apply colors to the layers of a variable color symbol, and you can choose whether to animate those changes from front-to-back, or back-to-front. SF Symbols 5 introduces layer groups, which allows related layers to move together when animated.

**Test animations for custom symbols.** It’s important to test your custom symbols with all of the animation presets because the shapes and paths might not appear how you expect when the layers are in motion. To get the most out of this feature, consider drawing your custom symbols with whole shapes. For example, a custom symbol similar to the `person.2.fill` symbol doesn’t need to create a cutout for the shape representing the person on the left. Instead, you can draw the full shape of the person, and in addition to that, draw an offset path of the person on the right to help represent the gap between them. This offset path can later be annotated as an erase layer to render the symbol as desired. This method of drawing helps preserve additional layer information that allow for animations to perform as expected.

**Avoid making custom symbols that include common variants, such as enclosures or badges.** The SF Symbols app offers a component library for creating variants of your custom symbol. Using the component library allows you to create commonly used variants of your custom symbol while maintaining design consistency with the included SF Symbols.

**Provide alternative text labels for custom symbols.** Alternative text labels — or accessibility descriptions — let VoiceOver describe visible UI and content, making navigation easier for people with visual disabilities. For guidance, see [VoiceOver](/design/human-interface-guidelines/accessibility#VoiceOver)
.

**Don’t design replicas of Apple products.** Apple products are copyrighted and you can’t reproduce them in your custom symbols. Also, you can’t customize a symbol that SF Symbols identifies as representing an Apple feature or product.

[Platform considerations](/design/human-interface-guidelines/sf-symbols#Platform-considerations)
------------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

[Resources](/design/human-interface-guidelines/sf-symbols#Resources)
--------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/sf-symbols#Related)

[SF Symbols](https://developer.apple.com/sf-symbols/)


[Typography](/design/human-interface-guidelines/typography)


#### [Developer documentation](/design/human-interface-guidelines/sf-symbols#Developer-documentation)

[Configuring and displaying symbol images in your UI](/documentation/uikit/uiimage/configuring_and_displaying_symbol_images_in_your_ui)


[Creating custom symbol images for your app](/documentation/uikit/uiimage/creating_custom_symbol_images_for_your_app)


[Symbols](/documentation/symbols)


#### [Videos](/design/human-interface-guidelines/sf-symbols#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/A5D5F4FB-B017-464E-92B2-1B9809572A36/8259_wide_250x141_1x.jpg) What’s new in SF Symbols 5](https://developer.apple.com/videos/play/wwdc2023/10197) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/80577069-4F0B-4756-96A0-B8F68156A39F/8325_wide_250x141_1x.jpg) Create animated symbols](https://developer.apple.com/videos/play/wwdc2023/10257) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/124/CB4DF3F4-EC99-4441-B517-BACD07A94347/6657_wide_250x141_1x.jpg) Adopt Variable Color in SF Symbols](https://developer.apple.com/videos/play/wwdc2022/10158) 
[Change log](/design/human-interface-guidelines/sf-symbols#Change-log)
----------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 5, 2023 | Added a new section on animations. Included animation guidance for custom symbols. |
| September 14, 2022 | Added a new section on variable color. Removed instructions on creating custom symbol paths, exporting templates, and layering paths, deferring to developer articles that cover these topics. |

