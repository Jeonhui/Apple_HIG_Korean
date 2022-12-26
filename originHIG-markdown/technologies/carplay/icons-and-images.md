# **[technologies-carplay] icons-and-images**

## **Image size and resolution**

The coordinate system CarPlay uses to place content onscreen is based on measurements in points, which map to pixels in the display. A standard-resolution display has a 1:1 pixel density (or @1x), where one pixel is equal to one point. High-resolution displays have a higher pixel density, offering a scale factor of 2.0 or 3.0 (referred to as @2x and @3x). As a result, high-resolution displays demand images with more pixels.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/ImageResolution-Graphic_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/ImageResolution-Graphic_2x.png)

For example, suppose you have a standard resolution (@1x) image that's 100px × 100px. The @2x version of this image would be 200px × 200px, and the @3x version would be 300px × 300px.

**Supply high-resolution images with scale factors of @2x and @3x for all CarPlay artwork in your app.** The system automatically shows the correct images and scales them appropriately, based on the resolution and size of the car’s display.

# **App icon**

Every CarPlay app needs a beautiful, memorable icon that stands out on the Home screen and is easy to tap while driving.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/audiobooks_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/audiobooks_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/maps_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/maps_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/message_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/message_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/music_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/music_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/now_playing_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/now_playing_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/phone_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/phone_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/podcasts_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icons/app_icons/podcasts_2x.png)

**Mirror your iPhone app icon.** A well-designed app icon works well in CarPlay and on iPhone, without the need for a second design.

**Don't use black for your icon’s background.** Lighten a black background or add a border so the icon doesn’t blend into the display background.

**Provide a single focus point.** Design an icon with a single, centered point that immediately captures attention and clearly identifies your app.

**Embrace simplicity.** Add details cautiously. If an icon’s content or shape is overly complex, the details can be hard to discern. Design an icon that instantly communicates your app’s purpose. For example, the Messages app icon uses a chat bubble, which is universally associated with messaging.

**Make sure your icon is opaque (not transparent), and keep the background simple.** Give your icon a simple background so it doesn’t overpower other app icons nearby. You don’t need to fill the entire icon with content.

**Use words only when they’re essential or part of a logo.** An app’s name appears below its icon on the Home screen. Don’t include nonessential words that repeat the name or tell people what to do with your app, like “Play.” If your design includes any text, emphasize words that relate to the actual content your app offers.

**Don’t include photos, screenshots, or interface elements.** Photographic details can be very hard to see at small sizes. Screenshots are too complex for an app icon and don’t generally help communicate your app’s purpose. Interface elements in an icon are misleading and confusing.

**Don’t place your app icon throughout the interface.** It can be confusing to see an icon used for different purposes throughout an app. Instead, consider incorporating your icon’s color scheme. See [Color](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/visual-design#color).

**Keep icon corners square.** The system applies a mask that rounds icon corners automatically.

For app icon design guidance, see [App icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

### **App icon sizes**

In addition to its iPhone app icons, your app must include CarPlay app icons in the following sizes.

---

120px by 120px (60pt by 60pt @2x)

---

180px by 180px (60pt by 60pt @3x)

---

# **Custom icons**

If your app includes tasks or modes that can’t be represented by an [SF Symbol](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols), or if you need icons that match your app’s style, you can create custom icons. A custom icon, sometimes called a template, discards color information and uses a mask to produce the appearance you see onscreen in a navigation bar or tab bar.

**Create simple, recognizable designs.** Too many details can make an icon appear sloppy or unreadable. Strive for a design most people will interpret correctly and won’t find offensive.

**Design a solid color icon with transparency, anti-aliasing, and no drop shadow.** The system ignores all color information, so there’s no need to use more than one fill color. Allow transparency to define the shape of the icon.

**Keep your icons consistent.** Whether you use only custom icons or mix custom and system icons, all icons in your app should be the same in terms of size, level of detail, perspective, and stroke weight. If you want an icon to look like it's related to the system icon family, use a very thin stroke to draw it. A 1-point stroke (2px for @2x, 3px for @3x) works well for most icons.

**Provide two versions of custom tab bar icons.** Provide icons for both the selected and unselected states. The selected icon is often a filled-in version of the unselected icon, but some designs call for variations to this approach. For example, Apple apps sometimes invert icon interiors, increase or reduce strokes, and enclose the icon within a shape, such as a circle.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/CustomIcon_Color_A.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/CustomIcon_Color_A.svg)

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/CustomIcon_Color_B.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/CustomIcon_Color_B.svg)

**Don’t use text in a tab bar icon.** If you need to show text, display a title beneath the tab and adjust its placement accordingly.

### **Custom icon sizes**

| Navigation bar icon size | Tab bar icons |
| --- | --- |
| 108px × 108px (36pt × 36pt @3x) | 108px × 108px (36pt × 36pt @3x) |
| 72px × 72px (36pt × 36pt @2x) | 72px × 72px (36pt × 36pt @2x) |