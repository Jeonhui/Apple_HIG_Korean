Lockups
=======

Lockups combine multiple separate views into a single, interactive unit.![A stylized representation of a person icon above a line of headline text and a line of footnote text. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/0d5e4d64c6d09fdf802bfebd9ffb5b0e/components-lockups-intro@2x.png)

Each lockup consists of a content view, a header, and a footer. Headers appear above the main content for a lockup, and footers appear below the main content. All three views expand and contract together as the lockup gets focus.

According to the needs of your app, you can combine four types of lockup: cards, caption buttons, monograms, and posters.

[Best practices](/design/human-interface-guidelines/lockups#Best-practices)
---------------------------------------------------------------------------

**Allow adequate space between lockups.** A focused lockup expands in size, so leave enough room between lockups to avoid overlapping or displacing other lockups. For guidance, see [Layout](/design/human-interface-guidelines/layout)
.

![An illustration showing three rows of five equally spaced lockups. In each row, the middle lockup is in focus and slightly larger than the others.](https://docs-assets.developer.apple.com/published/67a6f9b8d570939f21cd6af73ce21032/lockups-generic@2x.png)

**Use consistent lockup sizes within a row or group.** A group of buttons or a row of content images is more visually appealing when the widths and heights of all elements match.

For developer guidance, see [`TVLockupView`](/documentation/tvuikit/tvlockupview)
 and [`TVLockupHeaderFooterView`](/documentation/tvuikit/tvlockupheaderfooterview)
.

[Cards](/design/human-interface-guidelines/lockups#Cards)
---------------------------------------------------------

A card combines a header, footer, and content view to present ratings and reviews for media items.

![An illustration of an Apple TV screen that contains several cards, one of which is highlighted. Inside the highlighted card from the top, placeholder content shows the position of a rating and multiple lines of text.](https://docs-assets.developer.apple.com/published/697a2d112e491e9cf51cf654c70af8e4/lockups-background@2x.png)

For developer guidance, see [`TVCardView`](/documentation/tvuikit/tvcardview)


[Caption buttons](/design/human-interface-guidelines/lockups#Caption-buttons)
-----------------------------------------------------------------------------

A caption button can include a title and a subtitle beneath the button. A caption button can contain either an image or text.

Make sure that when people focus on them, caption buttons tilt with the motion that they swipe. When aligned vertically, caption buttons tilt up and down. When aligned horizontally, caption buttons tilt left and right. When displayed in a grid, caption buttons tilt both vertically and horizontally.

![An illustration of an Apple TV screen highlighted to show four caption buttons in a row. The leftmost button is focused, making it expand slightly and appear to float above the background.](https://docs-assets.developer.apple.com/published/338475f68a07a861939e2809a0211fbf/lockups-caption-button@2x.png)

For developer guidance, see [`TVCaptionButtonView`](/documentation/tvuikit/tvcaptionbuttonview)
.

[Monograms](/design/human-interface-guidelines/lockups#Monograms)
-----------------------------------------------------------------

Monograms identify people, usually the cast and crew for a media item. Each monogram consists of a circular picture of the person and their name. If an image isn’t available, the person’s initials appear in place of an image.

**Prefer images over initials.** An image of a person creates a more intimate connection than text.

![An illustration of an Apple TV screen that contains a row of several monograms, of which the leftmost one is highlighted. Each monogram contains the person symbol. Below each monogram is placeholder content that represents two lines of text.](https://docs-assets.developer.apple.com/published/906c0b8ed8e54f03b24792a684b3b449/lockups-monogram@2x.png)

For developer guidance, see [`TVMonogramContentView`](/documentation/tvuikit/tvmonogramcontentview)
.

[Posters](/design/human-interface-guidelines/lockups#Posters)
-------------------------------------------------------------

Posters consist of an image and an optional title and subtitle, which are hidden until the poster comes into focus. Posters can be any size, but the size needs to be appropriate for their content. For related guidance, see [Image views](/design/human-interface-guidelines/image-views)
.

![An illustration of an Apple TV screen that shows a row of several posters near the bottom edge. One poster is focused and below it is placeholder content that represents a line of text.](https://docs-assets.developer.apple.com/published/b37a0a55b2f3902282bd7464422ee054/lockups-poster@2x.png)

For developer guidance, see [`TVPosterView`](/documentation/tvuikit/tvposterview)


[Platform considerations](/design/human-interface-guidelines/lockups#Platform-considerations)
---------------------------------------------------------------------------------------------

*Not supported in iOS, iPadOS, macOS, visionOS, or watchOS.*

[Resources](/design/human-interface-guidelines/lockups#Resources)
-----------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/lockups#Related)

[Designing for tvOS](/design/human-interface-guidelines/designing-for-tvos)


[Layout](/design/human-interface-guidelines/layout)


#### [Developer documentation](/design/human-interface-guidelines/lockups#Developer-documentation)

[`TVLockupView`](/documentation/tvuikit/tvlockupview)


[`TVLockupHeaderFooterView`](/documentation/tvuikit/tvlockupheaderfooterview)


