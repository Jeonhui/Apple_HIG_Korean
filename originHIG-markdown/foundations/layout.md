# **[foundations] layout**

### Using a consistent layout that adapts to various contexts makes your experience more approachable and helps people enjoy their favorite apps and games on all their devices.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-layout-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-layout-intro-dark_2x.png)

# **Guides and safe areas**

A *layout guide* defines a rectangular region that helps you position, align, and space your content on the screen. The system includes predefined layout guides that make it easy to apply standard margins around content and restrict the width of text for optimal readability. You can also define custom layout guides.

A *safe area* defines the area within a view that isn’t covered by a navigation bar, tab bar, toolbar, or other views a window or scene might provide. Safe areas are essential for avoiding a device’s interactive and display features, like the Dynamic Island on iPhone or the camera housing on some Mac models.

In iOS, iPadOS, and tvOS, the system defines a collection of *traits* that characterize variations in the device environment that can affect the way your app displays on the screen. Using SwiftUI or Auto Layout, you can ensure that your interface adapts dynamically to a wide range of traits and contexts, including:

- Different device screen sizes, resolutions, and color spaces
- Different device orientations (portrait/landscape)
- Split view
- External display support, Display Zoom, and multitasking modes on iPad
- Dynamic Type text-size changes
- Internationalization features the system can enable based on locale (left-to-right/right-to-left layout direction, date/time/number formatting, font variation, text length)
- System feature availability

# **Best practices**

**Design a consistent layout that adapts gracefully to context changes, while displaying the same content as much as possible.** People expect your experience to work well and remain familiar when they rotate their device, resize a window, add another display, or switch to a different device. Ensure an adaptable interface by respecting system-defined safe areas, margins, and guides and specifying layout modifiers to fine-tune the placement of views in your hierarchy.

**Respect key display and system features in each platform.** Safe areas help you accommodate features like the corner radius and sensor housings on various devices, and avoid interfering with interactive system elements like Dynamic Island on iPhone and the Home indicator and app switcher on iPhone and iPad. Safe areas also help you account for interactive components like bars, dynamically repositioning content if sizes change.

**Use placement to convey relative importance.** In general, place principal items in the upper half of the screen or window, near the leading side. People typically start in this area, whether they’re looking at the screen or using a screen reader like VoiceOver.

**Elevate essential information by giving it sufficient space.** People want to view the most important information instantly, so you don’t want to clutter the screen or window with nonessential details. People can easily access secondary information by scrolling.

**Create visual groupings to help people find the information they want.** For example, you might use negative space, background shapes, colors, and materials, or separator lines to display related elements and information in distinct areas.

**Use alignment to ease visual scanning and to communicate organization and hierarchy.** Alignment makes an app look neat and organized, helps people focus while scrolling, and makes it easier to find information. Indentation and alignment can also help people visualize an information hierarchy.

**Be mindful of aspect ratio.** Different screen sizes may have different aspect ratios, causing artwork to appear cropped, letterboxed, or pillarboxed. When this is the case, don’t change the aspect ratio of the artwork; instead, scale it to fill the screen so that important visual content remains in view on all display sizes.

**Be prepared for text-size changes.** People expect most apps to respond when they choose a different text size. To accommodate text-size changes, you might need to adjust the layout. For guidance on displaying text in your app, see [Typography](https://developer.apple.com/design/human-interface-guidelines/foundations/typography).

**When possible, consider alluding to hidden content by partially displaying offscreen elements.** In large collections where content doesn’t fit on a single screen, you might be able to hint at the additional content by showing portions of the offscreen items.

**On touch screens, provide ample touch targets for interactive components.** Maintain a minimum tappable area of 44x44 points for all controls.

**Preview your app on multiple devices, using different orientations, localizations, and text sizes.** Although it’s generally best to preview features like wide color on actual devices, you can use Xcode Simulator to check for clipping and other layout issues. For example, if your iOS app supports landscape mode, you can use Simulator to make sure your layouts look great regardless of whether the device rotates left or right.

# **Platform considerations**

# **iOS, iPadOS**

**Aim to support both portrait and landscape orientations.** People choose different orientations for a variety of reasons, and they generally expect apps to work well in every context. If it’s essential that your app run in a single orientation, don’t tell people to rotate their device to match; if your app doesn’t rotate automatically when someone holds the device in an unsupported orientation, they’ll know instinctively to rotate it. If your app is landscape-only, make sure it runs equally well whether people rotate their device to the left or the right.

**If your app runs on a specific device, make sure it runs on every screen size for that device.** In other words, an iPhone-only app must run on every iPhone screen size and an iPad-only app must run on every iPad screen size. For guidance, see [Device screen sizes and orientations](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#device-screen-sizes-and-orientations).

**Inset full-width buttons.** Respect the standard system-defined margins on the sides of full-width buttons. A full-width button at the bottom of the screen generally looks best when it has rounded corners and it aligns with the bottom of the safe area — which also ensures that it doesn’t conflict with the Home indicator.

**Extend visual content to fill the screen.** Make sure backgrounds extend to the edges of the display, and that vertically scrollable layouts, like tables and collections, continue all the way to the bottom.

**On iPad, consider placing controls on the sides of the screen in landscape orientation.** When controls are on the left and right sides of the screen, people can reach them easily with both hands while they’re holding the device.

**Avoid placing interactive controls at the bottom edge of the screen when possible.** Regardless of orientation, people use system gestures at the bottom edge of the display to access features like the Home screen and app switcher, and these gestures may cancel custom gestures you implement in this area. Also avoid placing controls in the far corners of the screen because these areas can be difficult for people to reach comfortably. If your game needs to place controls in the lower portion of the screen — below the safe area — use matching insets when placing them at the top and bottom of the screen, and leave ample space around the Home indicator so people don’t accidentally target it when trying to interact with a control.

**Be prepared for different status bar heights.** If you display content below the status bar, you can use the safe area to help dynamically reposition the content as needed.

**Hide the status bar only when it adds value or enhances your experience.** The status bar displays information people find useful and it occupies an area of the screen most apps don’t fully use, so it’s generally a good idea to keep it visible.

### **iOS, iPadOS safe areas**

The safe area defines the area within a view that isn’t covered by a navigation bar, tab bar, toolbar, or other views a view controller might provide.

• [iPhone](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
• [iPad](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)

- 
    
    ![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-guides-portrait-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-guides-portrait-dark_2x.png)
    
    ![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-guides-landscape-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-guides-landscape-dark_2x.png)
    

### **iOS keyboard layout guide**

iOS 15 and later provides a keyboard layout guide that represents the space the keyboard currently occupies and accounts for safe area insets. Using this guide can help you make the keyboard feel like an integral part of your app, regardless of the type of keyboard people use or where they position it. For developer guidance, see [UIKeyboardLayoutGuide](https://developer.apple.com/documentation/uikit/uikeyboardlayoutguide/).

![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/keyboard-layout-guide-keyboard-visible-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/keyboard-layout-guide-keyboard-visible-dark_2x.png)

When the keyboard is visible, the layout guide represents its area and position.

![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/keyboard-layout-guide-keyboard-dismissed-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/keyboard-layout-guide-keyboard-dismissed-dark_2x.png)

When the keyboard dismisses, the top of the layout guide matches the bottom of the safe area layout guide.

# **macOS**

**Avoid placing controls or critical information at the bottom of a window.** People often move windows so that the bottom edge is below the bottom of the screen.

# **tvOS**

TVs vary widely in size. On Apple TV, app layouts don’t automatically adapt to the size of the screen like they do on iPhone or iPad. Instead, apps show the same interface on every display. Take extra care in designing your layout so that it looks great in a variety of screen sizes.

**Adhere to the screen’s safe zone.** Inset primary content 60 pixels from the top and bottom of the screen, and 80 pixels from the sides. It can be difficult for people to see content that close to the edges, and unintended cropping can occur due to overscanning on older TVs. Allow only partially displayed offscreen content and elements that deliberately flow offscreen to appear outside this zone.

![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/visual-design-safe-zone_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/visual-design-safe-zone_2x.png)

**Include appropriate padding between focusable elements.** When you use UIKit and the focus APIs, an element gets bigger when it comes into focus. Consider how elements look when they’re focused, and make sure they don’t unintentionally overlap important information.

![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/visual-design-padding_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/visual-design-padding_2x.png)

**Use layout templates to build media-centered apps and use grids to provide collections of content.** If the layout of your media app simply needs to present content beautifully with minimal layout customization, use a predesigned layout template. If your app needs to showcase a collection of content, use a grid to make the content easy to browse at a distance and quick to navigate with the remote.

### **Layout templates**

Apple TV templates deliver clean, consistent layouts that make content the center of attention. These templates — based on JavaScript and the Apple TV markup language (TVML) — dynamically load and populate with content when people open your app. Templates give you flexibility to create content-rich apps with predefined layouts that look good on the TV screen and are ideal for streaming media.

**Choose a template based on its purpose.** You can customize a template’s background, color, size, layout, and more, but if your customizations make the template jarring or unrecognizable, consider using a different one or designing a custom interface.

- 
    
    ![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/visual-design-templates-alert_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/visual-design-templates-alert_2x.png)
    
    ### **Alert Template**
    
    The alert template displays a message that asks for permission to perform an action, such as confirming a purchase or a destructive action like a deletion.See also [Alerts](https://developer.apple.com/design/human-interface-guidelines/tvos/interface-elements/alerts/).
    
- [Alert template](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
- [Catalog template](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
- [Compilation template](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
- [Descriptive alert template](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
- [Form template](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
- [List template](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
- [Loading template](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
- [Menu bar template](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
- [Parade template](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
- [Product template](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
- [Product bundle template](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
- [Rating template](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
- [Search template](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
- [Stack template](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)

**Customize templates tastefully.** Layout templates are highly customizable; you have control over the background, tinting, size, layout, and more. As you design your app, defer to content whenever possible, avoiding customizations that appear distracting, jarring, or obtrusive.

**Understand a template’s purpose before using it.** If your customizations make the underlying template unrecognizable, consider using a different template or building a custom interface.

For detailed information about integrating templates into your app, see [TVML](https://developer.apple.com/documentation/tvml).

### **Grids**

The following grid layouts provide an optimal viewing experience. Be sure to use appropriate spacing between unfocused rows and columns to prevent overlap when an item is brought into focus.

If you use the UIKit collection view flow element, the number of columns in a grid is automatically determined based on the width and spacing of your content. For developer guidance, see [UICollectionViewFlowLayout](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout).

• [Two-column](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
• [Three-column](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
• [Four-column](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
• [Five-column](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
• [Six-column](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
• [Seven-column](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
• [Eight-column](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)
• [Nine-column](https://developer.apple.com/design/human-interface-guidelines/foundations/layout#)

- 
    
    ![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/visual-design-grid-2-column_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/visual-design-grid-2-column_2x.png)
    
    ### **Two-Column Grid**
    

**Include additional vertical spacing for titled rows.** If a row has a title, provide enough spacing between the bottom of the previous unfocused row and the center of the title to avoid crowding. Also provide spacing between the bottom of the title and the top of the unfocused items in the row.

**Use consistent spacing.** When content isn’t consistently spaced, it no longer looks like a grid and it’s harder for people to scan.

**Make partially hidden content look symmetrical.** To help direct attention to the fully visible content, keep partially hidden offscreen content the same width on each side of the screen.

# **watchOS**

**Design your content to extend from one edge of the screen to the other.** The Apple Watch bezel provides a natural visual padding around your content. To avoid wasting valuable space, consider minimizing the padding between elements.

![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-full-width-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-full-width-dark_2x.png)

**Avoid placing more than two or three controls side by side in your interface.** As a general rule, display no more than three buttons that contain glyphs — or two buttons that contain text — in a row. Although it’s usually better to let text buttons span the full width of the screen, two side-by-side buttons with short text labels can also work well, as long as the screen doesn’t scroll.

![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-controls-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-controls-dark_2x.png)

**Support autorotation in views people might want to show others.** When people flip their wrist away, apps typically respond to the motion by sleeping the display, but in some cases it makes sense to autorotate the content. For example, a wearer might want to show an image to a friend or display a QR code to a reader. For developer guidance, see [isAutorotating](https://developer.apple.com/documentation/watchkit/wkextension/2868464-isautorotating).

# **Specifications**

# **iOS, iPadOS**

### **Device screen sizes and orientations**

**NOTE**All scale factors in the table above are UIKit scale factors, which may differ from native scale factors. For developer guidance, see [scale](https://developer.apple.com/documentation/uikit/uiscreen/1617836-scale) and [nativeScale](https://developer.apple.com/documentation/uikit/uiscreen/1617825-nativescale).

### **Device size classes**

Different size class combinations apply to the full-screen experience on different devices, based on screen size.

![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-size-classes_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-size-classes_2x.png)

On iPad, size classes also apply when your app or game runs in a [multitasking](https://developer.apple.com/design/human-interface-guidelines/patterns/multitasking) configuration.

![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-two-thirds.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-two-thirds.svg)

2/3 split view

![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-half.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-half.svg)

1/2 split view

![https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-thirds.svg](https://developer.apple.com/design/human-interface-guidelines/foundations/layout/images/layout-thirds.svg)

1/3 split view

# **watchOS**

| Device | Dimensions (portrait) |
| --- | --- |
| 12.9" iPad Pro | 1024x1366 pt (2048x2732 px @2x) |
| 11" iPad Pro | 834x1194 pt (1668x2388 px @2x) |
| 10.5" iPad Pro | 834x1194 pt (1668x2388 px @2x) |
| 9.7" iPad Pro | 768x1024 pt (1536x2048 px @2x) |
| 7.9" iPad mini | 768x1024 pt (1536x2048 px @2x) |
| 10.5" iPad Air | 834x1112 pt (1668x2224 px @2x) |
| 9.7" iPad Air | 768x1024 pt (1536x2048 px @2x) |
| 10.2" iPad | 810x1080 pt (1620x2160 px @2x) |
| 9.7" iPad | 768x1024 pt (1536x2048 px @2x) |
| iPhone 14 Pro Max | 430x932 pt (1290x2796 px @3x) |
| iPhone 14 Pro | 393x852 pt (1179x2556 px @3x) |
| iPhone 14 Plus | 428x926 pt (1284x2778 px @3x) |
| iPhone 14 | 390x844 pt (1170x2532 px @3x) |
| iPhone 13 Pro Max | 428x926 pt (1284x2778 px @3x) |
| iPhone 13 Pro | 390x844 pt (1170x2532 px @3x) |
| iPhone 13 | 390x844 pt (1170x2532 px @3x) |
| iPhone 13 mini | 375x812 pt (1125x2436 px @3x) |
| iPhone 12 Pro Max | 428x926 pt (1284x2778 px @3x) |
| iPhone 12 Pro | 390x844 pt (1170x2532 px @3x) |
| iPhone 12 | 390x844 pt (1170x2532 px @3x) |
| iPhone 12 mini | 375x812 pt (1125x2436 px @3x) |
| iPhone 11 Pro Max | 414x896 pt (1242x2688 px @3x) |
| iPhone 11 Pro | 375x812 pt (1125x2436 px @3x) |
| iPhone 11 | 414x896 pt (828x1792 px @2x) |
| iPhone XS Max | 414x896 pt (1242x2688 px @3x) |
| iPhone XS | 375x812 pt (1125x2436 px @3x) |
| iPhone XR | 414x896 pt (828x1792 px @2x) |
| iPhone X | 375x812 pt (1125x2436 px @3x) |
| iPhone 8 Plus | 414x736 pt (1080x1920 px @3x) |
| iPhone 8 | 375x667 pt (750x1334 px @2x) |
| iPhone 7 Plus | 414x736 pt (1080x1920 px @3x) |
| iPhone 7 | 375x667 pt (750x1334 px @2x) |
| iPhone 6s Plus | 414x736 pt (1080x1920 px @3x) |
| iPhone 6s | 375x667 pt (750x1334 px @2x) |
| iPhone 6 Plus | 414x736 pt (1080x1920 px @3x) |
| iPhone 6 | 375x667 pt (750x1334 px @2x) |
| 4.7" iPhone SE | 375x667 pt (750x1334 px @2x) |
| 4" iPhone SE | 320x568 pt (640x1136 px @2x) |
| iPod touch 5th generation and later | 320x568 pt (640x1136 px @2x) |

| Device | Portrait orientation | Landscape orientation |
| --- | --- | --- |
| 12.9" iPad Pro | Regular width, regular height | Regular width, regular height |
| 11" iPad Pro | Regular width, regular height | Regular width, regular height |
| 10.5" iPad Pro | Regular width, regular height | Regular width, regular height |
| 9.7" iPad | Regular width, regular height | Regular width, regular height |
| 7.9" iPad mini | Regular width, regular height | Regular width, regular height |
| iPhone 14 Pro Max | Compact width, regular height | Regular width, compact height |
| iPhone 14 Pro | Compact width, regular height | Compact width, regular height |
| iPhone 14 Plus | Compact width, regular height | Regular width, compact height |
| iPhone 14 | Compact width, regular height | Compact width, regular height |
| iPhone 13 Pro Max | Compact width, regular height | Regular width, compact height |
| iPhone 13 Pro | Compact width, regular height | Compact width, compact height |
| iPhone 13 | Compact width, regular height | Compact width, compact height |
| iPhone 13 mini | Compact width, regular height | Compact width, compact height |
| iPhone 12 Pro Max | Compact width, regular height | Regular width, compact height |
| iPhone 12 Pro | Compact width, regular height | Compact width, compact height |
| iPhone 12 | Compact width, regular height | Compact width, compact height |
| iPhone 12 mini | Compact width, regular height | Compact width, compact height |
| iPhone 11 Pro Max | Compact width, regular height | Regular width, compact height |
| iPhone 11 Pro | Compact width, regular height | Compact width, compact height |
| iPhone 11 | Compact width, regular height | Regular width, compact height |
| iPhone XS Max | Compact width, regular height | Regular width, compact height |
| iPhone XS | Compact width, regular height | Compact width, compact height |
| iPhone XR | Compact width, regular height | Regular width, compact height |
| iPhone X | Compact width, regular height | Compact width, compact height |
| iPhone 8 Plus | Compact width, regular height | Regular width, compact height |
| iPhone 8 | Compact width, regular height | Compact width, compact height |
| iPhone 7 Plus | Compact width, regular height | Regular width, compact height |
| iPhone 7 | Compact width, regular height | Compact width, compact height |
| iPhone 6s Plus | Compact width, regular height | Regular width, compact height |
| iPhone 6s | Compact width, regular height | Compact width, compact height |
| iPhone SE | Compact width, regular height | Compact width, compact height |
| iPod touch 5th generation and later | Compact width, regular height | Compact width, compact height |

| Device | Mode | Portrait orientation | Landscape orientation |
| --- | --- | --- | --- |
| 12.9" iPad Pro | 2/3 split view | Compact width, regular height | Regular width, regular height |
|  | 1/2 split view | N/A | Regular width, regular height |
|  | 1/3 split view | Compact width, regular height | Compact width, regular height |
| 11" iPad Pro | 2/3 split view | Compact width, regular height | Regular width, regular height |
|  | 1/2 split view | N/A | Compact width, regular height |
|  | 1/3 split view | Compact width, regular height | Compact width, regular height |
| 10.5" iPad Pro | 2/3 split view | Compact width, regular height | Regular width, regular height |
|  | 1/2 split view | N/A | Compact width, regular height |
|  | 1/3 split view | Compact width, regular height | Compact width, regular height |
| 9.7" iPad | 2/3 split view | Compact width, regular height | Regular width, regular height |
|  | 1/2 split view | N/A | Compact width, regular height |
|  | 1/3 split view | Compact width, regular height | Compact width, regular height |
| 7.9" iPad mini 4 | 2/3 split view | Compact width, regular height | Regular width, regular height |
|  | 1/2 split view | N/A | Compact width, regular height |
|  | 1/3 split view | Compact width, regular height | Compact width, regular height |

| Series | Screen size | Width (pixels) | Height (pixels) |
| --- | --- | --- | --- |
| Apple Watch Ultra | 49mm | 410 | 502 |
| 7 and later | 41 mm | 352 | 430 |
| 7 and later | 45 mm | 396 | 484 |
| 4, 5, and 6 | 40 mm | 324 | 394 |
| 4, 5, and 6 | 44 mm | 368 | 448 |
| 1, 2, and 3 | 38 mm | 272 | 340 |
| 1, 2, and 3 | 42 mm | 312 | 390 |