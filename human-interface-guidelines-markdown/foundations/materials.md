June 21, 2023

 Updated to include guidance for visionOS. Materials
=========

On Apple platforms, a material imparts translucency by blurring and modifying the color values of the underlying visual content.![A sketch of overlapping squares, suggesting the use of transparency to hint at background content. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/7dbd8b65138bed71acdeb36135193681/foundations-materials-intro@2x.png)

Translucency can improve the integration of foreground and background elements, visually communicating a separation between layers and helping people retain a sense of place. To enhance translucency, materials can combine with vibrancy. *Vibrancy* amplifies the sense of depth for foreground content like text, symbols, and fills, by pulling color forward from behind the material.

Note

Vibrancy can affect all apps and games — even ones that don’t display any vibrant views — because some components are vibrant by default, such as menus in macOS, windows in visionOS, and labels in iOS.

[Best practices](/design/human-interface-guidelines/materials#Best-practices)
-----------------------------------------------------------------------------

The system offers several materials that can automatically adapt to both light and dark appearances. In addition, you can apply system-provided blur and vibrancy effects to UI components to help them integrate well with materials and achieve the prominence you want. Using system-defined materials and effects can give your app or game a consistent appearance, and create smooth transitions when people switch between apps.

**Choose system materials and effects based on semantic meaning and recommended usage.** Avoid selecting a material or effect based on the apparent color it imparts to your interface, because system settings can change its appearance and behavior. Instead, match the material or vibrancy style to your specific use case. For example, use lighter materials to highlight interactive components in your visionOS app, the [menu](https://developer.apple.com/documentation/appkit/nsvisualeffectview/material/menu)
 material for a menu in your macOS app, the [label](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/label)
 vibrancy style for primary labels in your iOS app, and the [prominent](https://developer.apple.com/documentation/uikit/uiblureffect/style/prominent)
 material for adaptable, full-screen backgrounds in your tvOS app.

**Help ensure legibility by using vibrant colors on top of materials.** When you use system-defined vibrant colors, you don’t need to worry about colors seeming too dark, bright, saturated, or low contrast in different contexts. For example, iOS defines Dynamic System Colors for text, fills, symbols, and separators, making these items look great on translucent backgrounds. In macOS, all standard system colors have vibrant versions. In visionOS, the system uses the same dark vibrant colors that macOS uses, automatically adapting them to maintain contrast in different visual contexts. For guidance, see [Color](/design/human-interface-guidelines/color)
.

**Consider contrast and visual separation when choosing a material to combine with blur and vibrancy effects.** For example, consider that:

* Thicker materials can provide better contrast for text and other elements with fine features
* Translucency can help people retain their context by providing a visible reminder of the content that’s in the background

The system supplies several materials you can use to convey a sense of depth and hierarchical structure without distracting from content. Some of the materials adapt to appearance modes and some are always light or always dark. Regardless of the material you choose, you want to avoid using nonvibrant colors on top of it.

For developer guidance, see [`UIBlurEffect.Style`](/documentation/uikit/uiblureffect/style)
.

[Platform considerations](/design/human-interface-guidelines/materials#Platform-considerations)
-----------------------------------------------------------------------------------------------

### [iOS, iPadOS](/design/human-interface-guidelines/materials#iOS-iPadOS)

iOS and iPadOS define vibrancy values for labels, fills, and separators that are specifically designed to work with each material; standard system colors aren’t available in vibrant versions.

Labels and fills each provide several levels of vibrancy; separators have one level. The names of the levels indicate the relative amount of contrast between an element and the background: The default level has the highest contrast, whereas quaternary (when it exists) has the lowest contrast.

Except for quaternary, you can use the following vibrancy values for labels on any material. In general, avoid using quaternary on thin and ultra thin materials, because the contrast is too low.

* [`UIVibrancyEffectStyle.label`](/documentation/uikit/uivibrancyeffectstyle/label)
 (default)
* [`UIVibrancyEffectStyle.secondaryLabel`](/documentation/uikit/uivibrancyeffectstyle/secondarylabel)
* [`UIVibrancyEffectStyle.tertiaryLabel`](/documentation/uikit/uivibrancyeffectstyle/tertiarylabel)
* [`UIVibrancyEffectStyle.quaternaryLabel`](/documentation/uikit/uivibrancyeffectstyle/quaternarylabel)

You can use the following vibrancy values for fills on all materials.

* [`UIVibrancyEffectStyle.fill`](/documentation/uikit/uivibrancyeffectstyle/fill)
 (default)
* [`UIVibrancyEffectStyle.secondaryFill`](/documentation/uikit/uivibrancyeffectstyle/secondaryfill)
* [`UIVibrancyEffectStyle.tertiaryFill`](/documentation/uikit/uivibrancyeffectstyle/tertiaryfill)

The system provides a single, default vibrancy value for a [separator](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/separator)
, which works well on all materials.

### [macOS](/design/human-interface-guidelines/materials#macOS)

macOS provides vibrant versions of all standard colors, and provides materials that define the amounts of translucency, blurring, and vibrancy applied to your interface. The system provides several standard materials, each with a designated purpose. For example, you can choose a material to match the default look of a window, menu, popover, sidebar, title bar, and more. For developer guidance, see [`NSVisualEffectView.Material`](/documentation/appkit/nsvisualeffectview/material)
.

![The sidebar, window background, and selection materials display different amounts of transparency and blending in a light appearance.](https://docs-assets.developer.apple.com/published/904108c5cb735b367707dc286d473417/macos-light-appearance@2x.png)Light appearance![The sidebar, window background, and selection materials display different amounts of transparency and blending in a dark appearance.](https://docs-assets.developer.apple.com/published/dbf9234c84a8b4193936b2336a2b9165/macos-dark-appearance@2x.png)Dark appearance**Choose when to allow vibrancy in custom views and controls.** Depending on configuration and system settings, system views and controls use vibrancy to make foreground content stand out against any background. Test your interface in a variety of contexts to discover when vibrancy enhances the appearance and improves communication.

**Choose a background blending mode that complements your interface design.** macOS defines two modes that blend background content: behind window and within window. For developer guidance, see [`NSVisualEffectBlendingMode`](/documentation/appkit/nsvisualeffectblendingmode)
.

![The side bar of the Reminders app blends with the content behind the window.](https://docs-assets.developer.apple.com/published/e923613e161b76d5b09f06ff55e361dd/macos-behind-window-blending@2x.png)

**Behind-window blending.** In this mode, the content behind a window shows through, helping people retain some of the context that surrounds your app or game. Components such as menus, sheets, and sidebars automatically use this mode.

![The directions pane in Maps blends with the Map content from the window.](https://docs-assets.developer.apple.com/published/c6cabdf8d797535c17ea2e59d4ae74c2/macos-in-window-blending@2x.png)

**In-window blending.** This mode lets window content show through other window components. For example, a toolbar can use this mode to give people a sense of continuity as window content scrolls under it.

### [tvOS](/design/human-interface-guidelines/materials#tvOS)

**Use lighter, translucent materials to elevate content and make it feel fresh.** Darker materials tend to hide shadows, reducing depth and making it harder to distinguish content clearly. You might consider using darker materials if you want to evoke a heavier feeling or suggest that the content is older.

For example, consider using system materials in the following ways:



| Material | Recommended for | Adaptive behavior |
| --- | --- | --- |
| Prominent | Full-screen backgrounds | Displays the extra light material in the light appearance and the extra dark material in the dark appearance |
| Regular | Overlay views that partially obscure onscreen content | Displays the light material in the light appearance and the dark material in the dark appearance |
| Extra light | Full-screen views that require a light color scheme | – |
| Light | Overlay views that partially obscure onscreen content and require a light color scheme | – |
| Extra dark | Full-screen views that require a dark color scheme | – |
| Dark | Overlay views that partially obscure onscreen content and require a dark color scheme | – |

### [visionOS](/design/human-interface-guidelines/materials#visionOS)

In visionOS, windows generally use an unmodifiable system-defined material called *glass* that helps people stay grounded by letting light, the current Environment, virtual content, and objects in people’s surroundings show through. Glass is an adaptive material that limits the range of background color information so a window can continue to provide contrast for app content while becoming brighter or darker depending on people’s physical surroundings and other virtual content.

 [Play](#) 
Note

visionOS doesn’t have a distinct Dark Mode setting. Instead, glass automatically adapts to the luminance of the objects and colors behind it.

**Avoid using opaque colors in a window.** Areas of opacity can block people’s view, making them feel constricted and reducing their awareness of the virtual and physical objects around them.

**If necessary, choose materials that help you create visual separations or indicate interactivity in your app.** If you need to create a custom component, you may need to specify a system material for it. Use the following examples for guidance.

* Light materials bring attention to interactive elements like buttons and selected items.
* Dark materials can help you visually separate sections of your app, like a sidebar or a grouped table view.
* The darkest materials can give a component like a text field a recessed appearance that shows it’s an area that can accept text entry.

Note

A visionOS app uses light content by default, even though it also uses white text.

To ensure foreground content remains legible when it displays on top of a material, visionOS applies vibrancy to text, symbols, and fills. Vibrancy enhances the sense of depth by pulling light and color forward from both virtual and physical surroundings.

visionOS defines three vibrancy values that help you communicate a hierarchy of text, symbols, and fills.

* Use [`UIVibrancyEffectStyle.label`](/documentation/uikit/uivibrancyeffectstyle/label)
 for standard text.
* Use [`UIVibrancyEffectStyle.secondaryLabel`](/documentation/uikit/uivibrancyeffectstyle/secondarylabel)
 for descriptive text like footnotes and subtitles.
* Use [`UIVibrancyEffectStyle.tertiaryLabel`](/documentation/uikit/uivibrancyeffectstyle/tertiarylabel)
 for inactive elements, and only when text doesn’t need high legibility.

### [watchOS](/design/human-interface-guidelines/materials#watchOS)

**Use materials to provide context in a full-screen modal view.** Because full-screen modal views are common in watchOS, the contrast provided by material layers can help orient people in your app and distinguish controls and system elements from other content. Avoid removing or replacing material backgrounds for modal sheets when they’re provided by default.

[Resources](/design/human-interface-guidelines/materials#Resources)
-------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/materials#Related)

[Color](/design/human-interface-guidelines/color)


[Accessibility](/design/human-interface-guidelines/accessibility)


#### [Developer documentation](/design/human-interface-guidelines/materials#Developer-documentation)

[`Material`](/documentation/SwiftUI/Material)


[`UIVisualEffectView`](/documentation/uikit/uivisualeffectview)


[`NSVisualEffectView`](/documentation/appkit/nsvisualeffectview)


#### [Videos](/design/human-interface-guidelines/materials#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/48/0F960683-D91F-4CA9-9658-6FBB11F0683D/3272_wide_250x141_1x.jpg) What's New in iOS Design](https://developer.apple.com/videos/play/wwdc2019/808) 
[Change log](/design/human-interface-guidelines/materials#Change-log)
---------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |
| June 5, 2023 | Added guidance on using materials to provide context and orientation in watchOS apps. |

