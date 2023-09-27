Updated to include guidance for visionOS. Layout
======

A consistent layout that adapts to various contexts makes your experience more approachable and helps people enjoy their favorite apps and games on all their devices.![A sketch of a small rectangle in the upper-left quadrant of a larger rectangle, suggesting the position of a user interface element within a window. The image is overlaid with rectangular and circular grid lines and is tinted yellow to subtly reflect the yellow in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/fe3e14f290a6986d2490634a9e2fab0c/foundations-layout-intro@2x.png)

The following guidance helps you design content layouts for all platforms. To learn about displaying windows and other content throughout Apple Vision Pro space, see [Spatial layout](/design/human-interface-guidelines/spatial-layout)
.

[Guides and safe areas](/design/human-interface-guidelines/layout#Guides-and-safe-areas)
----------------------------------------------------------------------------------------

A *layout guide* defines a rectangular region that helps you position, align, and space your content on the screen. The system includes predefined layout guides that make it easy to apply standard margins around content and restrict the width of text for optimal readability. You can also define custom layout guides.

A *safe area* defines the area within a view that isn’t covered by a navigation bar, tab bar, toolbar, or other views a window or scene might provide. Safe areas are essential for avoiding a device’s interactive and display features, like the Dynamic Island on iPhone or the camera housing on some Mac models.

In iOS, iPadOS, tvOS, and visionOS, the system defines a collection of *traits* that characterize variations in the device environment that can affect the way your app looks. Using SwiftUI or Auto Layout, you can ensure that your interface adapts dynamically to a wide range of traits and contexts, including:

* Different device screen sizes, resolutions, and color spaces
* Different device orientations (portrait/landscape)
* Split view
* External display support, Display Zoom, and multitasking modes on iPad
* Dynamic Type text-size changes
* Locale-based internationalization features like left-to-right/right-to-left layout direction, date/time/number formatting, font variation, and text length
* System feature availability

[Best practices](/design/human-interface-guidelines/layout#Best-practices)
--------------------------------------------------------------------------

**Design a consistent layout that adapts gracefully to context changes, while displaying the same content as much as possible.** People expect your experience to work well and remain familiar when they rotate their device, resize a window, add another display, or switch to a different device. You can help ensure an adaptable interface by respecting system-defined safe areas, margins, and guides (where available) and specifying layout modifiers to fine-tune the placement of views in your hierarchy.

**Respect key display and system features in each platform.** Safe areas help you accommodate features like the corner radius and sensor housings on various devices, and avoid interfering with interactive system elements like Dynamic Island on iPhone and the Home indicator and app switcher on iPhone and iPad. Safe areas also help you account for interactive components like bars, dynamically repositioning content if sizes change.

**Use placement to convey relative importance.** People often start by viewing items in reading order — that is, from top to bottom and from the leading to trailing side — so it generally works well to place the most important items near the top and leading side of the window, display, or [field of view](/design/human-interface-guidelines/spatial-layout#Field-of-view)
.

**Make essential information easy to find by giving it sufficient space.** People want to view the most important information right away, so you don’t want to obscure it by crowding it with nonessential details. You can make secondary information available in other parts of the window or display.

**Create visual groupings to help people find the information they want.** For example, you might use negative space, background shapes, colors, materials, or separator lines to show when elements are related and to separate information into distinct areas.

**Use alignment to ease visual scanning and to communicate organization and hierarchy.** Alignment makes an app look neat and organized and can help people track content while scrolling or moving their eyes, making it easier to find information. Along with indentation, alignment can also help people understand an information hierarchy.

**Be prepared for text-size changes.** People expect most apps to respond when they choose a different text size. To accommodate text-size changes, you might need to adjust the layout. For guidance on displaying text in your app, see [Typography](/design/human-interface-guidelines/typography)
.

**Consider providing visual hints to help people discover content that’s currently hidden.** For example, if you can’t display all the items in a large collection at once, you need to indicate that there are additional items that aren’t currently visible. Depending on the platform, you might display parts of items to hint that people can reveal additional content by interacting with the view, such as by scrolling.

**Make interactive components easy to discover by providing enough space around them.** If interactive components are too close together — or if other content crowds them — the components can be difficult for people to distinguish, which can make your app or game hard to use.

**Preview your app on multiple devices, using different orientations, localizations, and text sizes.** Although it’s generally best to preview features like wide color on actual devices, you can use Xcode Simulator to check for clipping and other layout issues. For example, if your iOS app supports landscape mode, you can use Simulator to make sure your layouts look great regardless of whether the device rotates left or right.

**When necessary, scale artwork in response to display changes.** For example, viewing your app in a different context — such as on a screen with a different aspect ratio — might make your artwork appear cropped, letterboxed, or pillarboxed. If this happens, don’t change the aspect ratio of the artwork; instead, scale it so that important visual content remains visible. In visionOS, the system automatically [scales](/design/human-interface-guidelines/spatial-layout#Scale)
 a window when it moves along the z-axis.

[Platform considerations](/design/human-interface-guidelines/layout#Platform-considerations)
--------------------------------------------------------------------------------------------

### [iOS, iPadOS](/design/human-interface-guidelines/layout#iOS-iPadOS)

**Aim to support both portrait and landscape orientations.** People choose different orientations for a variety of reasons, and they generally expect apps to work well in every context. If it’s essential that your app run in a single orientation, don’t tell people to rotate their device to match; if your app doesn’t rotate automatically when someone holds the device in an unsupported orientation, they’ll know instinctively to rotate it. If your app is landscape-only, make sure it runs equally well whether people rotate their device to the left or the right.

**If your app runs on a specific device, make sure it runs on every screen size for that device.** In other words, an iPhone-only app must run on every iPhone screen size and an iPad-only app must run on every iPad screen size. For guidance, see [Device screen sizes and orientations](/design/human-interface-guidelines/layout#Device-screen-sizes-and-orientations)
.

**Inset full-width buttons.** Respect the standard system-defined margins on the sides of full-width buttons. A full-width button at the bottom of the screen generally looks best when it has rounded corners and it aligns with the bottom of the safe area — which also ensures that it doesn’t conflict with the Home indicator.

**Extend visual content to fill the screen.** Make sure backgrounds extend to the edges of the display, and that vertically scrollable layouts, like tables and collections, continue all the way to the bottom.

**On iPad, consider placing controls on the sides of the screen in landscape orientation.** When controls are on the left and right sides of the screen, people can reach them easily with both hands while they’re holding the device.

**Avoid placing interactive controls at the bottom edge of the screen when possible.** Regardless of orientation, people use system gestures at the bottom edge of the display to access features like the Home screen and app switcher, and these gestures may cancel custom gestures you implement in this area. Also avoid placing controls in the far corners of the screen because these areas can be difficult for people to reach comfortably. If your game needs to place controls in the lower portion of the screen — below the safe area — use matching insets when placing them at the top and bottom of the screen, and leave ample space around the Home indicator so people don’t accidentally target it when trying to interact with a control.

**Be prepared for different status bar heights.** If you display content below the status bar, you can use the safe area to help dynamically reposition the content as needed.

**Hide the status bar only when it adds value or enhances your experience.** The status bar displays information people find useful and it occupies an area of the screen most apps don’t fully use, so it’s generally a good idea to keep it visible.

#### [iOS, iPadOS safe areas](/design/human-interface-guidelines/layout#iOS-iPadOS-safe-areas)

The safe area defines the area within a view that isn’t covered by a navigation bar, tab bar, toolbar, or other views a view controller might provide.

* [iPhone](#)
* [iPad](#)
![An illustration of an iPhone in portrait orientation that displays a shaded rectangle, representing the safe area, and two vertical red strips at the left and right edges of the rectangle that represent margins.](https://docs-assets.developer.apple.com/published/d0c4b02329ef3e73ef068c00dd9aba3e/layout-guides-portrait@2x.png)

![An illustration of an iPhone in landscape orientation that displays a shaded rectangle, representing the safe area, and two vertical red strips at the left and right edges of the rectangle that represent margins.](https://docs-assets.developer.apple.com/published/3ac1ce8a02dc0a3babc7931748d62964/layout-guides-landscape@2x.png)

![An illustration of an iPad in portrait orientation that displays a shaded rectangle, representing the safe area, and two vertical red strips at the left and right edges of the rectangle that represent margins.](https://docs-assets.developer.apple.com/published/3f8a6632514396967be535fd7ec6e77d/safe-area-portrait@2x.png)

![An illustration of an iPad in landscape orientation that displays a shaded rectangle, representing the safe area, and two vertical red strips at the left and right edges of the rectangle that represent margins.](https://docs-assets.developer.apple.com/published/1bdc77161228ce6ed4fb5ef4105add66/safe-area-landscape@2x.png)

#### [iOS keyboard layout guide](/design/human-interface-guidelines/layout#iOS-keyboard-layout-guide)

iOS 15 and later provides a keyboard layout guide that represents the space the keyboard currently occupies and accounts for safe area insets. Using this guide can help you make the keyboard feel like an integral part of your app, regardless of the type of keyboard people use or where they position it. For developer guidance, see [`UIKeyboardLayoutGuide`](/documentation/uikit/uikeyboardlayoutguide)
.

![An illustration of an iPhone in portrait orientation. A shaded box labeled 'Safe area' appears over the top half of the screen. A shaded box labeled 'Keyboard layout guide' appears over the bottom half of the screen.](https://docs-assets.developer.apple.com/published/c4839fd59dcda19187412f2e7a68ff79/keyboard-layout-guide-keyboard-visible@2x.png)When the keyboard is visible, the layout guide represents its area and position.![An illustration of an iPhone in portrait orientation. A shaded box labeled 'Safe area' appears over most of the screen. A shaded box labeled 'Keyboard layout guide' appears over the very bottom of the screen.](https://docs-assets.developer.apple.com/published/a6497b7e936917ab450d89501add1cc6/keyboard-layout-guide-keyboard-dismissed@2x.png)When the keyboard dismisses, the top of the layout guide matches the bottom of the safe area layout guide.### [macOS](/design/human-interface-guidelines/layout#macOS)

**Avoid placing controls or critical information at the bottom of a window.** People often move windows so that the bottom edge is below the bottom of the screen.

### [tvOS](/design/human-interface-guidelines/layout#tvOS)

TVs vary widely in size. On Apple TV, app layouts don’t automatically adapt to the size of the screen like they do on iPhone or iPad. Instead, apps show the same interface on every display. Take extra care in designing your layout so that it looks great in a variety of screen sizes.

**Adhere to the screen’s safe zone.** Inset primary content 60 pixels from the top and bottom of the screen, and 80 pixels from the sides. It can be difficult for people to see content that close to the edges, and unintended cropping can occur due to overscanning on older TVs. Allow only partially displayed offscreen content and elements that deliberately flow offscreen to appear outside this zone.

![An illustration of a TV with a safe zone border on all sides. In width, the top and bottom borders measure 60 points, and the side borders both measure 80 points.](https://docs-assets.developer.apple.com/published/d70b487ffcb4619669866e367ef3abd4/visual-design-safe-zone@2x.png)

**Include appropriate padding between focusable elements.** When you use UIKit and the focus APIs, an element gets bigger when it comes into focus. Consider how elements look when they’re focused, and make sure they don’t unintentionally overlap important information.

![An illustration that uses vertical shaded rectangles to show padding between focusable items.](https://docs-assets.developer.apple.com/published/77f8f9af61ff8a2ccedf54808192c41b/visual-design-padding@2x.png)

**Use layout templates to build media-centered apps and use grids to provide collections of content.** If the layout of your media app simply needs to present content beautifully with minimal layout customization, use a predesigned layout template. If your app needs to showcase a collection of content, use a grid to make the content easy to browse at a distance and quick to navigate with the remote.

#### [Layout templates](/design/human-interface-guidelines/layout#Layout-templates)

Apple TV templates deliver clean, consistent layouts that make content the center of attention. These templates — based on JavaScript and the Apple TV markup language (TVML) — dynamically load and populate with content when people open your app. Templates give you flexibility to create content-rich apps with predefined layouts that look good on the TV screen and are ideal for streaming media.

**Choose a template based on its purpose.** You can customize a template’s background, color, size, layout, and more, but if your customizations make the template jarring or unrecognizable, consider using a different one or designing a custom interface.

* [Alert template](#)
* [Catalog template](#)
* [Compilation template](#)
* [Descriptive alert template](#)
* [Form template](#)
* [List template](#)
* [Loading template](#)
* [Menu bar template](#)
* [Parade template](#)
* [Product template](#)
* [Product bundle template](#)
* [Rating template](#)
* [Search template](#)
* [Stack template](#)
![An illustration of Apple TV, displaying the alert template.](https://docs-assets.developer.apple.com/published/8f439577b2a04a250c72277c0acb2eac/template-alert@2x.png)

#### [Alert template](/design/human-interface-guidelines/layout#Alert-template)

The alert template displays a message that asks for permission to perform an action, such as confirming a purchase or a destructive action like a deletion. See also [Alerts](/design/human-interface-guidelines/alerts)
.

![An illustration of Apple TV, displaying the catalog template.](https://docs-assets.developer.apple.com/published/30f65bd3c1005328d4a9338991250d68/template-catalog@2x.png)

#### [Catalog template](/design/human-interface-guidelines/layout#Catalog-template)

Use the catalog template to display groupings of related items, such as genres of movies or TV shows. People view the list of groupings on the left, and focus on one to see its items on the right.

![An illustration of Apple TV, displaying the compilation template.](https://docs-assets.developer.apple.com/published/976be9b4d4d910b61e2c6740d8c8418e/template-compilation@2x.png)

#### [Compilation template](/design/human-interface-guidelines/layout#Compilation-template)

The compilation template displays elements contained by an item, such as songs in an album or tracks in a playlist. This template works especially well to display audio-related content.

![An illustration of Apple TV, displaying the descriptive alert template.](https://docs-assets.developer.apple.com/published/b8d261022a1ecc10aba0f54c4984a35c/template-alert-descriptive@2x.png)

#### [Descriptive alert template](/design/human-interface-guidelines/layout#Descriptive-alert-template)

The descriptive alert template can show a lengthy message that may ask the reader to perform an action, such as agreeing to terms and conditions or reading a licensing agreement.

**Show, don’t tell.** Whenever possible, avoid descriptive alert text. Aim to present the same information in a more digestible way, such as with images.

**Keep alerts short and avoid making people scroll.** Reading lots of text on a distant screen strains the eyes and isn’t much fun. Minimize the amount of text your app displays.

**If the message is scrollable, position buttons side by side.** With this layout, scrolling up and down scrolls the text, while scrolling left and right switches focus between buttons.

For guidance, see [Alerts](/design/human-interface-guidelines/alerts)
.

![An illustration of Apple TV, displaying the form template.](https://docs-assets.developer.apple.com/published/bc6f55e3cf246a8dc04212460cfd8700/template-form@2x.png)

#### [Form template](/design/human-interface-guidelines/layout#Form-template)

The form template displays a keyboard and one or more text fields where viewers can enter information, such as a name or an email address. See also [Entering data](/design/human-interface-guidelines/entering-data)
.

![An illustration of Apple TV, displaying the list template.](https://docs-assets.developer.apple.com/published/36de8cfd3352a2a9f2ba50c8a4b2673c/template-list@2x.png)

#### [List template](/design/human-interface-guidelines/layout#List-template)

The list template shows a list of items on the right, such as movies or TV shows. People focus on one item to view its related content, such as its artwork or description, on the left.

![An illustration of Apple TV, displaying the loading template.](https://docs-assets.developer.apple.com/published/7a4ad1be026b80a17aa8f1b32885664d/template-loading@2x.png)

#### [Loading template](/design/human-interface-guidelines/layout#Loading-template)

The loading template temporarily displays a progress indicator and some descriptive text while the server retrieves your content. It lets people know something is happening, so your app doesn’t appear frozen.

**Keep loading text concise and informative.** If loading is quick, people may not have time to read longer text before it disappears, making them feel like they’ve missed something.

See also [Progress indicators](/design/human-interface-guidelines/progress-indicators)
.

![An illustration of Apple TV, displaying the menu bar template.](https://docs-assets.developer.apple.com/published/2a64269789f5d8fa80b9aede87990efd/template-menu-bar@2x.png)

#### [Menu bar template](/design/human-interface-guidelines/layout#Menu-bar-template)

The menu bar template is designed for top-level navigation, such as an entry page to your content. It includes a menu of items across the top. People focus on an item to view related content below the menu.

**Keep the menu bar uncluttered.** Each additional item you display adds more choices and increases the complexity of your app.

**Keep menu items onscreen.** When the menu bar is in focus, ensure that all of its items are visible. In general, include seven or fewer items with short labels, to avoid crowding content and causing items to scroll off the screen.

See also [Tab bars](/design/human-interface-guidelines/tab-bars)
.

![An illustration of Apple TV, displaying the parade template.](https://docs-assets.developer.apple.com/published/94cf04cae70d118dde509a46ca06b229/template-parade@2x.png)

#### [Parade template](/design/human-interface-guidelines/layout#Parade-template)

The parade template shows rotating previews for a focused grouping of content, such as movies or albums in a particular genre. A list of groupings is shown on the right. People focus on one grouping to view noninteractive rotating previews of its elements on the left.

![An illustration of Apple TV, displaying the product template.](https://docs-assets.developer.apple.com/published/dc1b7aab67ff656dc8db290ef31aa5e2/template-product@2x.png)

#### [Product template](/design/human-interface-guidelines/layout#Product-template)

The product template promotes movies, TV shows, or other products. It typically includes a product image, background, and descriptive information. A shelf below the product content displays related products, and people can scroll down to bring up more information, like cast and crew listings, ratings, and reviews.

**If you customize the background, make sure it doesn’t clash with your other content.** Consider image and text colors carefully before customizing the background. By default, the background displays a blurred copy of your product image, producing a complementary visual effect.

![An illustration of Apple TV, displaying the product bundle template.](https://docs-assets.developer.apple.com/published/7ab6b89ac3c69e52c2f95a941e5b98f6/template-product-bundle@2x.png)

#### [Product bundle template](/design/human-interface-guidelines/layout#Product-bundle-template)

The product bundle template promotes a series of related TV shows, movies, and other products. It typically includes an image, background, and descriptive information. A shelf below the content displays the products the bundle contains, such as the episodes of a TV season. People can scroll down to bring up more information, such as cast and crew listings, ratings, and reviews.

![An illustration of Apple TV, displaying the rating template.](https://docs-assets.developer.apple.com/published/c7c4ec8beb440abff033a768fc294325/template-rating@2x.png)

#### [Rating template](/design/human-interface-guidelines/layout#Rating-template)

The rating template lets people adjust the rating of a particular item, such as a movie or a song.

![An illustration of Apple TV, displaying the search template.](https://docs-assets.developer.apple.com/published/b600976ca0eec92f1c7666f92b54847d/template-search@2x.png)

#### [Search template](/design/human-interface-guidelines/layout#Search-template)

The search template lets people search your content and view results. It includes a search field, a keyboard, and a list of results.

![An illustration of Apple TV, displaying the stack template.](https://docs-assets.developer.apple.com/published/ed260fb6063fb3845960bc4bec42bddb/template-stack@2x.png)

#### [Stack template](/design/human-interface-guidelines/layout#Stack-template)

The stack template displays groups of products — such as different genres of movies — in rows. Each group of products displays directly beneath the previous group.

**Customize templates tastefully.** Layout templates are highly customizable; you have control over the background, tinting, size, layout, and more. As you design your app, defer to content whenever possible, avoiding customizations that appear distracting, jarring, or obtrusive.

**Understand a template’s purpose before using it.** If your customizations make the underlying template unrecognizable, consider using a different template or building a custom interface.

For detailed information about integrating templates into your app, see [TVML](/documentation/TVML)
.

#### [Grids](/design/human-interface-guidelines/layout#Grids)

The following grid layouts provide an optimal viewing experience. Be sure to use appropriate spacing between unfocused rows and columns to prevent overlap when an item is brought into focus.

If you use the UIKit collection view flow element, the number of columns in a grid is automatically determined based on the width and spacing of your content. For developer guidance, see [`UICollectionViewFlowLayout`](/documentation/uikit/uicollectionviewflowlayout)
.

* [Two-column](#)
* [Three-column](#)
* [Four-column](#)
* [Five-column](#)
* [Six-column](#)
* [Seven-column](#)
* [Eight-column](#)
* [Nine-column](#)
![An illustration of Apple TV, displaying a two-column grid of media items. Additional media items are partially visible on the right side and bottom edge of the screen.](https://docs-assets.developer.apple.com/published/d577c3ac4e484d949c170cfa505073c4/visual-design-grid-2-column@2x.png)

#### [Two-column grid](/design/human-interface-guidelines/layout#Two-column-grid)



| Attribute | Value |
| --- | --- |
| Unfocused content width | 860 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

![An illustration of Apple TV, displaying a three-column grid of media items. Additional media items are partially visible on the right side and bottom edge of the screen.](https://docs-assets.developer.apple.com/published/d6d33c16e558689e5df794a40240030e/visual-design-grid-3-column@2x.png)

#### [Three-column grid](/design/human-interface-guidelines/layout#Three-column-grid)



| Attribute | Value |
| --- | --- |
| Unfocused content width | 560 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

![An illustration of Apple TV, displaying a four-column grid of media items. Additional media items are partially visible on the right side of the screen.](https://docs-assets.developer.apple.com/published/53465d4cbf4d54bf7f54a1fe0aad69c2/visual-design-grid-4-column@2x.png)

#### [Four-column grid](/design/human-interface-guidelines/layout#Four-column-grid)



| Attribute | Value |
| --- | --- |
| Unfocused content width | 410 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

![An illustration of Apple TV, displaying a five-column grid of media items. Additional media items are partially visible on the right side and bottom edge of the screen.](https://docs-assets.developer.apple.com/published/7729a9baf067e70d987871466c875829/visual-design-grid-5-column@2x.png)

#### [Five-column grid](/design/human-interface-guidelines/layout#Five-column-grid)



| Attribute | Value |
| --- | --- |
| Unfocused content width | 320 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

![An illustration of Apple TV, displaying a six-column grid of media items. Additional media items are partially visible on the right side and bottom edge of the screen.](https://docs-assets.developer.apple.com/published/363166bc22bb12746940ac6a0ee47d9f/visual-design-grid-6-column@2x.png)

#### [Six-column grid](/design/human-interface-guidelines/layout#Six-column-grid)



| Attribute | Value |
| --- | --- |
| Unfocused content width | 260 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

![An illustration of Apple TV, displaying a seven-column grid of media items. Additional media items are partially visible on the right side of the screen.](https://docs-assets.developer.apple.com/published/d2129f4b27dc80a9d7528f9cb382a477/visual-design-grid-7-column@2x.png)

#### [Seven-column grid](/design/human-interface-guidelines/layout#Seven-column-grid)



| Attribute | Value |
| --- | --- |
| Unfocused content width | 217 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

![An illustration of Apple TV, displaying an eight-column grid of media items. Additional media items are partially visible on the right side and bottom edge of the screen.](https://docs-assets.developer.apple.com/published/ba74e699570d39b4c7d4142f9abfb8b2/visual-design-grid-8-column@2x.png)

#### [Eight-column grid](/design/human-interface-guidelines/layout#Eight-column-grid)



| Attribute | Value |
| --- | --- |
| Unfocused content width | 184 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

![An illustration of Apple TV, displaying a nine-column grid of media items.](https://docs-assets.developer.apple.com/published/32367e6123252d802948995cccab7fb0/visual-design-grid-9-column@2x.png)

#### [Nine-column grid](/design/human-interface-guidelines/layout#Nine-column-grid)



| Attribute | Value |
| --- | --- |
| Unfocused content width | 160 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Include additional vertical spacing for titled rows.** If a row has a title, provide enough spacing between the bottom of the previous unfocused row and the center of the title to avoid crowding. Also provide spacing between the bottom of the title and the top of the unfocused items in the row.

**Use consistent spacing.** When content isn’t consistently spaced, it no longer looks like a grid and it’s harder for people to scan.

**Make partially hidden content look symmetrical.** To help direct attention to the fully visible content, keep partially hidden offscreen content the same width on each side of the screen.

### [visionOS](/design/human-interface-guidelines/layout#visionOS)

The guidance below can help you lay out content within the windows of your visionOS app or game, making it feel familiar and easy to use. For guidance on displaying windows in space and best practices for using depth, scale, and field of view in your visionOS app, see [Spatial layout](/design/human-interface-guidelines/spatial-layout)
. To learn more about visionOS window components, see [Windows > visionOS](/design/human-interface-guidelines/windows#visionOS)
.

Note

When you add depth to content in a standard window, the content extends beyond the window’s bounds along the z-axis. If content extends too far along the z-axis, the system clips it.

**Keep a window’s content within its bounds.** In visionOS, the system displays window controls just outside a window’s bounds in the XY plane. For example, the Share menu appears above the window and the controls for resizing, moving, and closing the window appear below it. Letting 2D or 3D content encroach on these areas can make the system-provided controls, especially those below the window, difficult for people to use.

**In general, avoid placing important content and controls in a window’s corners.** The farther content is from the center of a window, the more difficult it can be for people to see and interact with it, especially when the window is large.

**Make a window’s interactive components easy for people to focus.** You need to include enough space around an interactive component so that focusing it is easy and comfortable, and to prevent the system-provided hover effect from obscuring other content. For example, place buttons so their centers are at least 60 points apart. For guidance, see [Eyes](/design/human-interface-guidelines/eyes)
, [Spatial layout](/design/human-interface-guidelines/spatial-layout)
, and [Buttons > visionOS](/design/human-interface-guidelines/buttons#visionOS)
.

**If you need to display additional controls that don’t belong within a window, use an ornament.** An ornament lets you offer app controls that remain visually associated with a window without interfering with the system-provided controls. For example, a window’s toolbar and tab bar appear as ornaments. For guidance, see [Ornaments](/design/human-interface-guidelines/ornaments)
.

### [watchOS](/design/human-interface-guidelines/layout#watchOS)

**Design your content to extend from one edge of the screen to the other.** The Apple Watch bezel provides a natural visual padding around your content. To avoid wasting valuable space, consider minimizing the padding between elements.

![An illustration of the Workout app’s main list of workouts on Apple Watch. A callout indicates that the currently focused workout item spans the full width of the available screen area.](https://docs-assets.developer.apple.com/published/180d82ec20b9f85908474cc931d4707e/layout-full-width@2x.png)

**Avoid placing more than two or three controls side by side in your interface.** As a general rule, display no more than three buttons that contain glyphs — or two buttons that contain text — in a row. Although it’s usually better to let text buttons span the full width of the screen, two side-by-side buttons with short text labels can also work well, as long as the screen doesn’t scroll.

![A diagram of an Apple Watch screen showing two side-by-side buttons beneath three lines of text.](https://docs-assets.developer.apple.com/published/aa5904c73a0b5295604bb551c164325c/layout-controls@2x.png)

**Support autorotation in views people might want to show others.** When people flip their wrist away, apps typically respond to the motion by sleeping the display, but in some cases it makes sense to autorotate the content. For example, a wearer might want to show an image to a friend or display a QR code to a reader. For developer guidance, see [`isAutorotating`](/documentation/watchkit/wkextension/2868464-isautorotating)
.

[Specifications](/design/human-interface-guidelines/layout#Specifications)
--------------------------------------------------------------------------

### [iOS, iPadOS](/design/human-interface-guidelines/layout#iOS-iPadOS)

#### [Device screen sizes and orientations](/design/human-interface-guidelines/layout#Device-screen-sizes-and-orientations)



| Device | Dimensions (portrait) |
| --- | --- |
| 12.9” iPad Pro | 1024x1366 pt (2048x2732 px @2x) |
| 11” iPad Pro | 834x1194 pt (1668x2388 px @2x) |
| 10.5” iPad Pro | 834x1194 pt (1668x2388 px @2x) |
| 9.7” iPad Pro | 768x1024 pt (1536x2048 px @2x) |
| 7.9” iPad mini | 768x1024 pt (1536x2048 px @2x) |
| 10.5” iPad Air | 834x1112 pt (1668x2224 px @2x) |
| 9.7” iPad Air | 768x1024 pt (1536x2048 px @2x) |
| 10.2” iPad | 810x1080 pt (1620x2160 px @2x) |
| 9.7” iPad | 768x1024 pt (1536x2048 px @2x) |
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
| 4.7” iPhone SE | 375x667 pt (750x1334 px @2x) |
| 4” iPhone SE | 320x568 pt (640x1136 px @2x) |
| iPod touch 5th generation and later | 320x568 pt (640x1136 px @2x) |

Note

All scale factors in the table above are UIKit scale factors, which may differ from native scale factors. For developer guidance, see [`scale`](/documentation/uikit/uiscreen/1617836-scale)
 and [`nativeScale`](/documentation/uikit/uiscreen/1617825-nativescale)
.

#### [Device size classes](/design/human-interface-guidelines/layout#Device-size-classes)

Different size class combinations apply to the full-screen experience on different devices, based on screen size.

![An illustration of an iPad and an iPhone in both portrait and landscape orientations. Each device in each orientation includes a red screen and arrowed lines that indicate the full height and width of the screen.](https://docs-assets.developer.apple.com/published/ea27d20bc28241ad815bbca4b92b9b71/layout-size-classes@2x.png)



| Device | Portrait orientation | Landscape orientation |
| --- | --- | --- |
| 12.9” iPad Pro | Regular width, regular height | Regular width, regular height |
| 11” iPad Pro | Regular width, regular height | Regular width, regular height |
| 10.5” iPad Pro | Regular width, regular height | Regular width, regular height |
| 9.7” iPad | Regular width, regular height | Regular width, regular height |
| 7.9” iPad mini | Regular width, regular height | Regular width, regular height |
| iPhone 14 Pro Max | Compact width, regular height | Regular width, compact height |
| iPhone 14 Pro | Compact width, regular height | Compact width, compact height |
| iPhone 14 Plus | Compact width, regular height | Regular width, compact height |
| iPhone 14 | Compact width, regular height | Compact width, compact height |
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

On iPad, size classes also apply when your app or game runs in a [multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking)
 configuration.

![An illustration of iPad in landscape orientation with the left two-thirds of its screen shaded.](https://docs-assets.developer.apple.com/published/e2c436a11b4dd3636828c6c3844465b2/layout-two-thirds@2x.png)2/3 split view![An illustration of iPad in landscape orientation with the left half of its screen shaded.](https://docs-assets.developer.apple.com/published/976669fb0a060433ac179c23d4728186/layout-half@2x.png)1/2 split view![An illustration of iPad in landscape orientation with the left one-third of its screen shaded.](https://docs-assets.developer.apple.com/published/f25f319072f994822c92d9ffa63bf9c8/layout-thirds@2x.png)1/3 split view

| Device | Mode | Portrait orientation | Landscape orientation |
| --- | --- | --- | --- |
| 12.9” iPad Pro | 2/3 split view | Compact width, regular height | Regular width, regular height |
|  | 1/2 split view | N/A | Regular width, regular height |
|  | 1/3 split view | Compact width, regular height | Compact width, regular height |
| 11” iPad Pro | 2/3 split view | Compact width, regular height | Regular width, regular height |
|  | 1/2 split view | N/A | Compact width, regular height |
|  | 1/3 split view | Compact width, regular height | Compact width, regular height |
| 10.5” iPad Pro | 2/3 split view | Compact width, regular height | Regular width, regular height |
|  | 1/2 split view | N/A | Compact width, regular height |
|  | 1/3 split view | Compact width, regular height | Compact width, regular height |
| 9.7” iPad | 2/3 split view | Compact width, regular height | Regular width, regular height |
|  | 1/2 split view | N/A | Compact width, regular height |
|  | 1/3 split view | Compact width, regular height | Compact width, regular height |
| 7.9” iPad mini 4 | 2/3 split view | Compact width, regular height | Regular width, regular height |
|  | 1/2 split view | N/A | Compact width, regular height |
|  | 1/3 split view | Compact width, regular height | Compact width, regular height |

### [watchOS](/design/human-interface-guidelines/layout#watchOS)



| Series | Screen size | Width (pixels) | Height (pixels) |
| --- | --- | --- | --- |
| Apple Watch Ultra | 49mm | 410 | 502 |
| 7 and later | 41mm | 352 | 430 |
| 7 and later | 45mm | 396 | 484 |
| 4, 5, and 6 | 40mm | 324 | 394 |
| 4, 5, and 6 | 44mm | 368 | 448 |
| 1, 2, and 3 | 38mm | 272 | 340 |
| 1, 2, and 3 | 42mm | 312 | 390 |

[Resources](/design/human-interface-guidelines/layout#Resources)
----------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/layout#Related)

[Right to left](/design/human-interface-guidelines/right-to-left)


#### [Developer documentation](/design/human-interface-guidelines/layout#Developer-documentation)

[`UITraitCollection`](/documentation/uikit/uitraitcollection)


[`UITraitEnvironment`](/documentation/uikit/uitraitenvironment)


[Responding to changing display modes on Apple TV](/documentation/uikit/app_and_environment/responding_to_changing_display_modes_on_apple_tv)


#### [Videos](/design/human-interface-guidelines/layout#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/48/0F960683-D91F-4CA9-9658-6FBB11F0683D/3272_wide_250x141_1x.jpg) What's New in iOS Design](https://developer.apple.com/videos/play/wwdc2019/808) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/7/2546ECBD-6443-41EC-921D-6429026F8B67/1700_wide_250x141_1x.jpg) Essential Design Principles](https://developer.apple.com/videos/play/wwdc2017/802) 
[Change log](/design/human-interface-guidelines/layout#Change-log)
------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | Added specifications for iPhone 14 Pro Max, iPhone 14 Pro, iPhone 14 Plus, iPhone 14, and Apple Watch Ultra. |

