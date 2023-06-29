# **[components-layout-and-organization] lockups**

# Lockups combine multiple separate views into a single, interactive unit.
> 잠금 기능은 여러 개의 개별 보기를 하나의 대화형 장치로 결합합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/lockups-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/lockups-intro-dark_2x.png)

Each lockup consists of a content view, a header, and a footer. Headers appear above the main content for a lockup, and footers appear below the main content. All three views expand and contract together as the lockup gets focus.
> 각 잠금은 내용 보기, 머리글 및 바닥글로 구성됩니다. 헤더는 잠금을 위한 기본 내용 위에 나타나고 바닥글은 기본 내용 아래에 나타납니다. 잠금이 초점을 맞추면 세 가지 보기가 모두 함께 확장되고 축소됩니다.
>




According to the needs of your app, you can combine four types of lockup: cards, caption buttons, monograms, and posters.
> 앱의 필요에 따라 카드, 캡션 버튼, 모노그램 및 포스터의 네 가지 잠금 유형을 결합할 수 있습니다.
>




# **Best practices**

**Allow adequate space between lockups.** A focused lockup expands in size, so leave enough room between lockups to avoid overlapping or displacing other lockups. For guidance, see [Layout](../foundations/layout).
> 잠금 사이에 충분한 공간을 확보하십시오. 집중 잠금 크기는 확장되므로 다른 잠금 장치가 겹치거나 이동하지 않도록 잠금 장치 사이에 충분한 공간을 두십시오. 자세한 내용은 레이아웃을 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-generic-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-generic-dark_2x.png)

**Use consistent lockup sizes within a row or group.** A group of buttons or a row of content images is more visually appealing when the widths and heights of all elements match.
> 행 또는 그룹 내에서 일관된 잠금 크기를 사용하십시오. 모든 요소의 폭과 높이가 일치할 때 단추 그룹이나 내용 이미지 행이 시각적으로 더 매력적입니다.
>




For developer guidance, see [TVLockupView](https://developer.apple.com/documentation/tvuikit/tvlockupview) and [TVLockupHeaderFooterView](https://developer.apple.com/documentation/tvuikit/tvlockupheaderfooterview).

# **Cards**

A card combines a header, footer, and content view to present ratings and reviews for media items.
> 카드는 머리글, 바닥글 및 내용 보기를 결합하여 미디어 항목에 대한 등급 및 검토를 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-background_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-background_2x.png)

For developer guidance, see [TVCardView.](https://developer.apple.com/documentation/tvuikit/tvcardview)

## **Caption buttons**

A caption button can include a title and a subtitle beneath the button. A caption button can contain either an image or text.
> 캡션 단추는 단추 아래에 제목과 부제를 포함할 수 있습니다. 캡션 버튼은 이미지 또는 텍스트를 포함할 수 있습니다.
>




Make sure that when people focus on them, caption buttons tilt with the motion that they swipe. When aligned vertically, caption buttons tilt up and down. When aligned horizontally, caption buttons tilt left and right. When displayed in a grid, caption buttons tilt both vertically and horizontally.
> 사람들이 그들에게 초점을 맞출 때, 그들이 스와이프하는 동작과 함께 캡션 버튼이 기울어지도록 하세요. 세로로 정렬하면 캡션 단추가 위아래로 기울어집니다. 수평으로 정렬하면 캡션 단추가 왼쪽과 오른쪽으로 기울어집니다. 그리드에 표시될 때 캡션 단추는 수직 및 수평으로 기울어집니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-caption-button_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-caption-button_2x.png)

For developer guidance, see[TVCaptionButtonView.](https://developer.apple.com/documentation/tvuikit/tvcaptionbuttonview)

# **Monograms**

Monograms identify people, usually the cast and crew for a media item. Each monogram consists of a circular picture of the person and their name. If an image isn't available, the person's initials appear in place of an image.
> 모노그램은 보통 미디어 아이템의 출연진과 제작진을 식별한다. 각 모노그램은 그 사람과 그 사람의 이름의 원형 그림으로 구성되어 있다. 이미지를 사용할 수 없는 경우 이미지 대신 사용자의 이니셜이 나타납니다.
>




**Prefer images over initials.** An image of a person creates a more intimate connection than text.
> 이니셜보다 이미지를 선호합니다. 사람의 이미지는 텍스트보다 더 친밀한 연결을 만듭니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-monogram_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-monogram_2x.png)

For developer guidance, see[TVMonogramContentView.](https://developer.apple.com/documentation/tvuikit/tvmonogramcontentview)

# **Posters**

Posters consist of an image and an optional title and subtitle, which are hidden until the poster comes into focus. Posters can be any size, but the size should be appropriate for their content. For related guidance, see [Image views](../components/content/image-views).
> 포스터는 이미지와 선택적 제목 및 부제로 구성되며, 포스터에 초점이 맞춰질 때까지 숨겨집니다. 포스터는 어떤 크기라도 될 수 있지만, 크기는 그 내용에 적합해야 한다. 관련 지침은 이미지 보기를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-poster_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/lockups/images/lockups-poster_2x.png)

For developer guidance, see [TVPosterView.](https://developer.apple.com/documentation/tvuikit/tvposterview)

# **Platform considerations**

*Not supported in iOS, iPadOS, macOS, or watchOS.*
> iOS, iPadOS, macOS 또는 watch에서 지원되지 않음OS.
>



