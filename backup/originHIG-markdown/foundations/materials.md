# **[foundations] materials**

### On Apple platforms, a material imparts translucency and blurring to a background, creating a sense of visual separation between foreground and background layers.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-materials-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-materials-intro-dark_2x.png)

Materials can combine with vibrancy to add visual interest to the interface. *Vibrancy* applies to foreground content that displays on top of a material — such as text, symbols, and fills — and works by pulling color forward from behind the material to enhance the sense of depth.

**NOTE**Vibrancy can affect all apps and games — even ones that don’t display any vibrant views — because some components are vibrant by default, such as menus in macOS and labels in iOS.

# **Best practices**

The system defines several materials — each intended for a specific usage — that automatically adapt to both light and dark modes. In addition, the system provides several blur and vibrancy effects you can apply to UI components to help them integrate well with materials and achieve the prominence you want. Using system-defined materials and effects can give your app or game a native feel, and create smooth transitions when people switch between apps.

**Choose system materials and effects based on semantic meaning and recommended usage.** Avoid selecting a material or effect based on the apparent color it imparts to your interface, because system settings can change its appearance and behavior. Instead, match the material or style to your specific use case. For example, use the [menu](https://developer.apple.com/documentation/appkit/nsvisualeffectview/material/menu) material for a menu in your macOS app, use the [label](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/label) vibrancy style for primary labels in your iOS app, and use the [prominent](https://developer.apple.com/documentation/uikit/uiblureffect/style/prominent) material for adaptable, full-screen backgrounds in your tvOS app.

**Help ensure legibility by using only vibrant colors on top of materials.** When you use system-defined vibrant colors, you don’t need to worry about colors seeming too dark, bright, saturated, or low contrast in different contexts. For example, iOS defines Dynamic System Colors for text, fills, glyphs, and separators, making these items look great on translucent backgrounds. In macOS, all standard system colors have vibrant versions. For guidance, see [Color](https://developer.apple.com/design/human-interface-guidelines/foundations/color).

**Consider using SF Symbols instead of full-color icons.** Full-color images may not have sufficient contrast with a view’s background, making them seem out of place when the background is translucent, whereas symbols and interface icons work with dynamic system colors and vibrancy effects to look good in any context. For guidance, see [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols).

**Consider contrast and visual separation when choosing a material to combine with blur and vibrancy effects.** For example, consider that:

- Thicker materials can provide better contrast for text and other elements with fine features
- Translucency can help people retain their context by providing a visible reminder of the content that’s in the background

The system supplies several materials you can use to convey a sense of depth and hierarchical structure without distracting from content. Ranging from ultra thin to ultra thick, some of the materials adapt to appearance modes and some are always light or always dark. Regardless of the material you choose, you want to avoid using non-vibrant colors on top of it.

For developer guidance, see [UIBlurEffect.Style](https://developer.apple.com/documentation/uikit/uiblureffect/style).

# **Platform considerations**

*Not supported in watchOS.*

# **iOS, iPadOS**

iOS and iPadOS define vibrancy values for labels, fills, and separators that are specifically designed to work with each material; standard system colors aren’t available in vibrant versions.

Labels and fills each provide several levels of vibrancy; separators have one level. The names of the levels indicate the relative amount of contrast between an element and the background: the default level has the highest contrast, whereas quaternary (when it exists) has the lowest contrast.

Except for quaternary, you can use the following vibrancy values for labels on any material. It's not recommended to use quaternary on thin and ultra thin materials, because the contrast is too low.

- [label](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/label) (default)
- [secondaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondarylabel)
- [tertiaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiarylabel)
- [quaternaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/quaternarylabel)

You can use the following vibrancy values for fills on all materials.

- [fill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/fill) (default)
- [secondaryFill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondaryfill)
- [tertiaryFill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiaryfill)

The system provides a single, default vibrancy value for a [separator](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/separator), which works well on all materials.

# **macOS**

macOS provides vibrant versions of all standard colors, and provides materials that define the amounts of translucency, blurring, and vibrancy applied to your interface. The system provides several standard materials, each with a designated purpose. For example, you can choose a material to match the default look of a window, menu, popover, sidebar, title bar, and more. For developer guidance, see [NSVisualEffectView.Material](https://developer.apple.com/documentation/appkit/nsvisualeffectview/material).

![https://developer.apple.com/design/human-interface-guidelines/foundations/materials/images/macos-light-appearance_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/materials/images/macos-light-appearance_2x.png)

Light appearance

![https://developer.apple.com/design/human-interface-guidelines/foundations/materials/images/macos-dark-appearance_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/materials/images/macos-dark-appearance_2x.png)

Dark appearance

**Choose when to allow vibrancy in custom views and controls.** Depending on configuration and system settings, system views and controls use vibrancy to make foreground content stand out against any background. Test your interface in a variety of contexts to discover when vibrancy enhances the appearance and improves communication.

**Choose a background blending mode that complements your interface design.** macOS defines two modes that blend background content: behind window and within window. For developer guidance, see [NSVisualEffectBlendingMode](https://developer.apple.com/documentation/appkit/nsvisualeffectblendingmode).

![https://developer.apple.com/design/human-interface-guidelines/foundations/materials/images/macos-behind-window-blending_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/materials/images/macos-behind-window-blending_2x.png)

**Behind-window blending.** In this mode, the content behind a window shows through, helping people retain some of the context that surrounds your app or game. Components such as menus, sheets, and sidebars automatically use this mode.

![https://developer.apple.com/design/human-interface-guidelines/foundations/materials/images/macos-in-window-blending_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/materials/images/macos-in-window-blending_2x.png)

**In-window blending.** This mode lets window content show through other window components. For example, a toolbar can use this mode to give people a sense of continuity as window content scrolls under it.

# **tvOS**

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