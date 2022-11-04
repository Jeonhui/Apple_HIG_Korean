# **[components-layout-and-organization] lockups**

# Lockups combine multiple separate views into a single, interactive unit.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/lockups-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/lockups-intro-dark_2x.png)

Each lockup consists of a content view, a header, and a footer. Headers appear above the main content for a lockup, and footers appear below the main content. All three views expand and contract together as the lockup gets focus.

According to the needs of your app, you can combine four types of lockup: cards, caption buttons, monograms, and posters.

# **Best practices**

**Allow adequate space between lockups.** A focused lockup expands in size, so leave enough room between lockups to avoid overlapping or displacing other lockups. For guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/foundations/layout).

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-generic-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-generic-dark_2x.png)

**Use consistent lockup sizes within a row or group.** A group of buttons or a row of content images is more visually appealing when the widths and heights of all elements match.

For developer guidance, see [TVLockupView](https://developer.apple.com/documentation/tvuikit/tvlockupview) and [TVLockupHeaderFooterView](https://developer.apple.com/documentation/tvuikit/tvlockupheaderfooterview).

# **Cards**

A card combines a header, footer, and content view to present ratings and reviews for media items.

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-background_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-background_2x.png)

For developer guidance, see [TVCardView.](https://developer.apple.com/documentation/tvuikit/tvcardview)

## **Caption buttons**

A caption button can include a title and a subtitle beneath the button. A caption button can contain either an image or text.

Make sure that when people focus on them, caption buttons tilt with the motion that they swipe. When aligned vertically, caption buttons tilt up and down. When aligned horizontally, caption buttons tilt left and right. When displayed in a grid, caption buttons tilt both vertically and horizontally.

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-caption-button_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-caption-button_2x.png)

For developer guidance, see[TVCaptionButtonView.](https://developer.apple.com/documentation/tvuikit/tvcaptionbuttonview)

# **Monograms**

Monograms identify people, usually the cast and crew for a media item. Each monogram consists of a circular picture of the person and their name. If an image isn't available, the person's initials appear in place of an image.

**Prefer images over initials.** An image of a person creates a more intimate connection than text.

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-monogram_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-monogram_2x.png)

For developer guidance, see[TVMonogramContentView.](https://developer.apple.com/documentation/tvuikit/tvmonogramcontentview)

# **Posters**

Posters consist of an image and an optional title and subtitle, which are hidden until the poster comes into focus. Posters can be any size, but the size should be appropriate for their content. For related guidance, see [Image views](https://developer.apple.com/design/human-interface-guidelines/components/content/image-views).

![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-poster_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-poster_2x.png)

For developer guidance, see [TVPosterView.](https://developer.apple.com/documentation/tvuikit/tvposterview)

# **Platform considerations**

*Not supported in iOS, iPadOS, macOS, or watchOS.*