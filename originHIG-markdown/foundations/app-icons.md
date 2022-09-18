# **[foundations] app-icons**

### A unique, memorable icon communicates the purpose and personality of your experience and can help people recognize your app or game at a glance in the App Store and on their devices.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-app-icons-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/foundations/foundations-app-icons-intro-dark_2x.png)

Beautiful app icons are an important part of the user experience on all Apple platforms and every app and game must have one. Each platform defines a slightly different style for app icons, so you want to create a design that adapts well to different shapes and levels of detail while maintaining strong visual consistency and messaging. To download templates that help you create icons for each platform see [Apple Design Resources](https://developer.apple.com/design/resources/). For guidance on creating other types of icons, see [Icons](https://developer.apple.com/design/human-interface-guidelines/foundations/icons/).

# **Best practices**

**Embrace simplicity.** Simple icons tend to be easier for people to understand and recognize. Find a concept or element that captures the essence of your app or game, make it the focus point of the icon, and express it in a simple, unique way. Avoid adding too many details, because they can be hard to discern and can make an icon appear muddy, especially at smaller sizes. Prefer a simple background that puts the emphasis on the primary image — you don’t need to fill the entire icon with content.

**Create a design that works well on multiple platforms so that it feels at home on each.** If your app or game runs on more than one platform, use a similar image and color palette for all icons while rendering them in the style that’s appropriate for each platform. For example, in iOS and watchOS, the Mail app icon uses a streamlined, graphical style to depict the white envelope on a blue background; macOS uses a similar blue background, adding depth and detail to the envelope, giving it a realistic weight and texture.

**Prefer including text only when it’s an essential part of your experience or brand.** Text in icons is often too small to read easily, can make an icon appear cluttered, and doesn’t support accessibility or localization. In some contexts, the app name appears near the icon, making it redundant to display the name within it. Although using a mnemonic like the first letter of your app’s name can help people recognize your app or game, avoid including nonessential words that tell people what to do with it — like "Watch" or "Play" — or context-specific terms like "New" or "For iOS."

**Prefer graphical images to photos and avoid replicating UI components in your icon.** Photos are full of details that don’t work well when viewed at small sizes. Instead of using a photo, create a graphic representation of the content that emphasizes the features you want people to notice. Similarly, if your app has an interface that people recognize, don’t just replicate standard UI components or use app screenshot in your icon.

**If needed, optimize your icon for the specific sizes the system displays in places like Spotlight search results, Settings, and notifications.** For iOS, iPadOS, and watchOS, you can tell Xcode to generate all sizes from your 1024×1024 px App Store icon, or you can provide assets for some or all individual icon sizes. For macOS and tvOS, you need to supply all sizes. If you want to forego the system-generated versions of your app icon and instead create your own, make sure the image remains clear as icon size decreases. For example, you might remove fine details and unnecessary features, simplifying the image and exaggerating primary features. In general, it’s best to make subtle changes so that your app icon remains visually consistent in every context.

![https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/app-icon-sizes_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/app-icon-sizes_2x.png)

The 512x512 px Safari app icon (on the left) uses a circle of tick marks to indicate degrees; the 16x16 px version of the icon (on the right) doesn’t include this detail.

**Design your icon as a full-bleed square image.** On most platforms, the system applies a mask that automatically adjusts icon corners to match the platform’s aesthetic. For example, watchOS automatically applies a circular mask. The exception is macOS: Although the system applies the rounded rectangle appearance to the icon of an app created with Mac Catalyst, you need to create your macOS app icon in the correct shape. For downloadable production templates that help you create app icons for each platform, see [Apple Design Resources](https://developer.apple.com/design/resources/).

**Consider offering an alternate app icon.** In iOS, iPadOS, and tvOS, people can choose an alternate version of an icon, which can strengthen their connection with the app or game and enhance their experience. For example, a sports app might offer different icons for different teams. Make sure that each alternate app icon you design remains closely related to your content and experience; avoid creating a version that people might mistake for the icon of a different app. When people want to switch to an alternate icon, they can visit your app’s settings.

**NOTE**As with a primary app icon, alternate app icons are also subject to app review and must adhere to the [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/#design).

**Don’t use replicas of Apple hardware products.** Apple products are copyrighted and can’t be reproduced in your app icons.

# **Platform considerations**

# **iOS, iPadOS**

**Don’t add an overlay or border to your Settings icon.** iOS automatically adds a 1-pixel stroke to all icons so that they look good on the white background of Settings.

# **macOS**

In macOS, app icons share a common set of visual attributes, including a rounded-rectangle shape, front-facing perspective, level position, and uniform drop shadow. Rooted in the macOS design language, these attributes showcase the lifelike rendering style people expect in macOS while presenting a harmonious user experience.

**Consider depicting a familiar tool to communicate what people use your app to do.** To give context to your app’s purpose, you can use the icon background to portray the tool’s environment or the items it affects. For example, the TextEdit icon pairs a mechanical pencil with a sheet of lined paper to suggest a utilitarian writing experience. After you create a detailed, realistic image of a tool, it often works well to let it float just above the background and extend slightly past the icon boundaries. If you do this, make sure the tool remains visually unified with the background and doesn’t overwhelm the rounded-rectangle shape.

![https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/app-icon-familiar-tool_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/app-icon-familiar-tool_2x.png)

**If you depict real objects in your app icon, make them look like they’re made of physical materials and have actual mass.** Consider replicating the characteristics of substances like fabric, glass, paper, and metal to convey an object’s weight and feel. For example, the Xcode app icon features a hammer that looks like it has a steel head and polymer grip.

![https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/app-icon-realistic-materials_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/app-icon-realistic-materials_2x.png)

**Use the drop shadow in the icon-design template.** The app-icon [template](https://developer.apple.com/design/resources/#macos-apps) includes the system-defined drop shadow that helps your app icon coordinate with other macOS icons.

**Consider using interior shadows and highlights to add definition and realism.** For example, the Mail app icon uses both shadows and highlights to give the envelope authenticity and to suggest that the flap is slightly open. In icons that include a tool that floats above a background — such as TextEdit or Xcode — interior shadows can strengthen the perception of depth and make the tool look real. Shadows and highlights should suggest a light source that faces the icon, positioned just above center and tilted slightly downward.

**Avoid defining contours that suggest a shape other than a rounded rectangle.** In rare cases, you might want to fine-tune the basic app icon shape, but doing so risks creating an icon that looks like it doesn’t belong in macOS. If you must alter the shape, prefer subtle adjustments that continue to express a rounded rectangle silhouette.

![https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/app-icon-consistent-shape_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/app-icon-consistent-shape_2x.png)

**Keep primary content within the icon grid bounding box; keep all content within the outer bounding box.** If an icon’s primary content extends beyond the icon grid bounding box, it tends to look out of place. If you overlay a tool on your icon, it works well to align the tool’s top edge with the outer bounding box and its bottom edge with the inner bounding box, as shown below. You can use the grid to help you position items within an icon and to ensure that centered inner elements like circles use a size that’s consistent with other icons in the system.

![https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/app-icon-layout-guides_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/app-icon-layout-guides_2x.png)

# **tvOS**

tvOS app icons use between two and five layers to create a sense of depth and vitality as people bring them into focus. For guidance, see [Layered images](https://developer.apple.com/design/human-interface-guidelines/foundations/images#layered-images).

**Use appropriate layer separation.** If your icon includes a logo, separate the logo from the background. If your icon includes text, bring the text to the front so it’s not hidden by other layers when the parallax effect occurs.

![https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/icons-and-images-icon-structure_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/icons-and-images-icon-structure_2x.png)

**Use gradients and shadows cautiously.** Background gradients and vignettes can clash with the parallax effect. For gradients, prefer top-to-bottom, light-to-dark styles. Shadows usually look best as sharp, hard-edged tints that are baked into the background layer and aren’t visible when the app icon is stationary.

**Leverage varying opacity levels to increase the sense of depth and liveliness.** Creative use of opacity can make your icon stand out. For example, the Photos icon separates its centerpiece into multiple layers that contain translucent pieces, bringing greater liveliness to the design.

**Make sure your Home Screen icon adheres to safe-zone specifications.** During focus and parallax, the system may crop content around the edges of your app icon as the icon scales and moves. To ensure your icon’s content isn’t cropped too tightly, allow some additional space as shown in [Specifications > tvOS](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons#tvos-app-icon-sizes).

# **watchOS**

A watchOS app icon is circular and displays no accompanying text.

![https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/icon-and-image-large-icon-mail-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/icon-and-image-large-icon-mail-dark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/icon-and-image-large-icon-fitness-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/icon-and-image-large-icon-fitness-dark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/icon-and-image-large-icon-settings-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons/images/icon-and-image-large-icon-settings-dark_2x.png)

**Avoid using black for your icon’s background.** Lighten a black background or add a border so the icon doesn’t blend into the display background.

# **Specifications**

# **App icon attributes**

App icons in all platforms use the PNG format and support the following color spaces:

- Display P3 (wide-gamut color)
- sRGB (color)
- Gray Gamma 2.2 (grayscale)

The layers, transparency, and corner radius of an app icon can vary per platform. Specifically:

# **App icon sizes**

### **iOS, iPadOS app icon sizes**

You need to provide a large version of your app icon, measuring 1024x1024 pixels, to display in the App Store. You can let the system automatically scale down your large app icon to produce all other sizes, or — if you want to customize the appearance of the icon at specific sizes — you can supply multiple versions.

### **macOS app icon sizes**

For the App Store, create a 1024x1024 px version of your macOS app icon. In addition, you also need to supply the icon in the following sizes.

### **tvOS app icon sizes**

For the App Store, create a 1280x768 px version of your tvOS app icon. In addition, you also need to supply the icon in the following sizes.

**Consider allowing a safe zone in your Home Screen icon.** During focus and parallax, content around the edges of your app icon may be cropped as the icon scales and moves. To ensure your icon’s content isn’t cropped too tightly, you might want to include some additional breathing room.

### **watchOS app icon sizes**

For the App Store, create a 1024x1024 px version of your watchOS app icon. You can let the system automatically scale this version down to all other sizes, or — if you want to customize the appearance of your app icon at specific sizes — you can supply the sizes listed in the following table. All icon dimensions are shown in pixels @2x.

If you have a companion iPhone app, you also need to supply your watchOS app icon in the following sizes.

| Platform | Layers | Transparency | Asset shape |
| --- | --- | --- | --- |
| iOS, iPadOS | Single | No | Square |
| macOS | Single | Yes, as appropriate | Square with rounded corners |
| tvOS | Multiple | No | Rectangle |
| watchOS | Single | No | Square |

| @2x (pixels) | @3x (pixels) iPhone only | Usage |
| --- | --- | --- |
| 120x120 | 180x180 | Home Screen on iPhone |
| 167x167 | – | Home Screen on iPad Pro |
| 152x152 | – | Home Screen on iPad, iPad mini |
| 80x80 | 120x120 | Spotlight on iPhone, iPad Pro, iPad, iPad mini |
| 58x58 | 87x87 | Settings on iPhone, iPad Pro, iPad, iPad mini |
| 76x76 | 114x114 | Notifications on iPhone, iPad Pro, iPad, iPad mini |

| @1x (pixels) | @2x (pixels) |
| --- | --- |
| 512x512 | 1024x1024 |
| 256x256 | 512x512 |
| 128x128 | 256x256 |
| 32x32 | 64x64 |
| 16x16 | 32x32 |

| @1x (pixels) | @2x (pixels) | Usage |
| --- | --- | --- |
| 400x240 | 800x480 | Home Screen |

| 38mm | 40mm | 41mm | 42mm | 44mm | 45mm | 49mm | Usage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 80x80 | 88x88 | 92x92 | 80x80 | 100x100 | 102x102 | 108x108 | Home Screen |
| 48x48 | 55x55 | 58x58 | 55x55 | 58x58 | 66x66 | 66x66 | Notification Center |
| 172x172 | 196x196 | 196x196 | 196x196 | 216x216 | 234x234 | 258x258 | Short look |

| @2x (pixels) | @3x (pixels) |
| --- | --- |
| 58x58 | 87x87 |