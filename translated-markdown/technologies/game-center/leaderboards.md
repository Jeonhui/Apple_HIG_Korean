# **[technologies-game-center] leaderboards**

Leaderboards can be a great way to encourage competition within your game. When you adopt Game Center and provide the relevant data, players can easily check their ranking against friends or global players.
> 리더보드는 게임 내에서 경쟁을 유도하는 좋은 방법이 될 수 있습니다. 게임센터를 채택해 관련 데이터를 제공하면 플레이어는 친구나 글로벌 플레이어와 순위를 쉽게 확인할 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/leaderboards_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/leaderboards_2x.png)

You can take advantage of the system-designed UI or present leaderboard information within custom UI. If necessary, you can also provide a custom link that takes players directly to the leaderboards area in the dashboard. For guidance, see [Custom dashboard links](../technologies/game-center/custom-dashboard-links).
> 시스템 설계 UI를 활용하거나 사용자 정의 UI 내에서 리더보드 정보를 제공할 수 있습니다. 필요한 경우 대시보드의 리더보드 영역으로 직접 이동하는 사용자 지정 링크를 제공할 수도 있습니다. 자세한 내용은 사용자 지정 대시보드 링크를 참조하십시오.
>




**Choose a leaderboard type that aligns with the core mechanics of your game.** Game Center supports a classic leaderboard that tracks all-time scores and a recurring leaderboard that resets based on an interval you define. For example, you might want your leaderboard to reset every other week, every day, or even every 5 minutes. Recurring leaderboards can increase engagement by giving players more chances to take the lead. For developer guidance, see [GKLeaderboard](https://developer.apple.com/documentation/gamekit/gkleaderboard).
> 게임의 핵심 메커니즘에 맞는 리더보드 유형을 선택하십시오. 게임 센터는 역대 점수를 추적하는 클래식 리더보드와 사용자가 정의한 간격에 따라 재설정되는 반복 리더보드를 지원합니다. 예를 들어, 리더보드를 격주, 매일 또는 5분마다 재설정할 수 있습니다. 반복적인 리더보드는 플레이어가 주도권을 잡을 수 있는 기회를 더 많이 제공하여 참여도를 높일 수 있습니다. 개발자 지침은 GK Leaderboard를 참조하십시오.
>




# **Creating leaderboard images (optional)**

Although you don’t have to supply leaderboard images, doing so gives you another opportunity to offer beautiful artwork and reinforce your game’s visual aesthetic.
> 리더보드 이미지를 제공할 필요는 없지만, 그렇게 하면 아름다운 예술작품을 제공하고 게임의 시각적 아름다움을 강화할 수 있는 또 다른 기회를 얻을 수 있습니다.
>




**Design high-quality artwork that echoes the in-game experience.** Players should be able to recognize your leaderboards at a glance.
> 게임 내 경험을 반영하는 고품질 아트워크를 디자인합니다. 플레이어는 리더보드를 한눈에 알아볼 수 있어야 합니다.
>




**Aim to create a unique image for each leaderboard.** People often use these images to help them distinguish among leaderboards, so it’s a good idea to avoid reusing an image in multiple leaderboards. As you design individual images, keep in mind that players often see several leaderboards at the same time, so prefer complimentary images that work well as a set.
> 각 리더보드마다 고유한 이미지를 만드는 것을 목표로 합니다. 사람들은 종종 이러한 이미지를 사용하여 리더보드를 구분하므로 여러 리더보드에서 이미지를 재사용하지 않는 것이 좋습니다. 개별 이미지를 디자인할 때 플레이어는 종종 여러 개의 리더보드를 동시에 볼 수 있으므로 세트로 잘 작동하는 무료 이미지를 선호합니다.
>




**Create leaderboard images in the appropriate size and format.** For games that run in iOS, iPadOS, and macOS, the system displays an individual leaderboard at its actual size, except for rounding both top corners. For leaderboards that are part of a set, the system crops the top and bottom of each image, leaving a rectangular area in the middle. To ensure that your primary content remains visible, make sure it stays within the cropped rectangle.
> 적절한 크기와 형식으로 리더보드 이미지를 만듭니다. iOS, iPadOS 및 macOS에서 실행되는 게임의 경우 시스템은 양쪽 상단 모서리를 반올림하는 것을 제외하고 실제 크기로 개별 리더보드를 표시합니다. 집합의 일부인 리더보드의 경우 시스템은 각 이미지의 상단과 하단을 잘라내고 가운데에 직사각형 영역을 남깁니다. 기본 내용을 계속 표시하려면 잘린 사각형 안에 있어야 합니다.
>




Use the following specifications to create leaderboard artwork for a game that runs in iOS, iPadOS, and macOS.
> 다음 사양을 사용하여 iOS, iPadOS 및 MacOS에서 실행되는 게임의 리더보드 아트워크를 만들 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/leaderboard-image-layout-general_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/leaderboard-image-layout-general_2x.png)

| Attribute | Value |
| --- | --- |
| Format | PNG or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 512x512 pt (1024x1024 px @2x) |
| Cropped area | 512x320 pt (1024x640 px @2x) |

For games that run in tvOS, provide between one and three multilayer images for each leaderboard or leaderboard set in your game. The back layer of the art must be opaque. At runtime, a dark gradient may overlay your image from bottom to top, and you can place text above the bottom-right corner. Unlike achievement images, leaderboard images are focusable.
> TVOS에서 실행되는 게임의 경우 게임의 각 리더보드 또는 리더보드 세트에 대해 하나에서 세 개의 다층 이미지를 제공합니다. 예술의 이면은 불투명해야 한다. 실행 시 어두운 그라데이션이 아래에서 위로 이미지를 덮어쓸 수 있으며, 텍스트를 오른쪽 아래 모서리 위에 배치할 수 있습니다. 성과 이미지와 달리 리더보드 이미지는 초점을 맞출 수 있습니다.
>




Because they’re focusable, you need to design leaderboards that remain easy to view while the focus effect moves and scales the images (to learn more about focus effects, see [Focus and selection](../inputs/focus-and-selection)). In addition, focusing may crop your leaderboard content at the edges of some layers. To ensure that your primary content stays comfortably visible while in focus, avoid placing it too close to the edges.
> 포커스가 가능하기 때문에 포커스 효과가 이미지를 이동하고 크기를 조정하는 동안 보기 쉬운 리더보드를 설계해야 합니다(포커스 효과에 대한 자세한 내용은 포커스 및 선택 참조). 또한 포커스를 맞추는 것은 일부 레이어의 가장자리에서 리더보드 내용을 자를 수 있습니다. 초점이 맞춰져 있는 동안 기본 콘텐츠가 편안하게 표시되도록 하려면 가장자리에 너무 가까이 두지 마십시오.
>




Use the following specifications to create leaderboard images for a game that runs in tvOS. You can also download a template from [Apple Design Resources](https://developer.apple.com/design/resources/#tvos-apps) that can help you position content.
> 다음 사양을 사용하여 tvOS에서 실행되는 게임의 리더보드 이미지를 만들 수 있습니다. 또한 Apple Design Resources에서 콘텐츠를 배치하는 데 도움이 되는 템플릿을 다운로드할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/tvos-multi-layered-leaderboard-image_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/tvos-multi-layered-leaderboard-image_2x.png)

| Attribute | Value |
| --- | --- |
| Aspect ratio | 16:9 |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 659x371 pt (1318x742 px @2x) |
| Focused size | 618x348 pt (1236x696 px @2x) |
| Unfocused size | 548x309 pt (1096x618 px @2x) |

# **Writing text that describes your leaderboards**
> 리더보드를 설명하는 텍스트 작성
>




A leaderboard includes a title you can use to describe the area of competition.
> 리더보드에는 경기 영역을 설명하는 데 사용할 수 있는 제목이 포함되어 있습니다.
>




**Be succinct and use correct capitalization.** A leaderboard truncates the title after two lines of text. Use title-style capitalization for the title and avoid capitalizing all letters.
> 간결하고 올바른 대소문자를 사용하십시오. 리더보드는 두 줄의 텍스트 뒤에 제목을 잘라냅니다. 제목에 제목 스타일 대문자를 사용하고 모든 문자를 대문자로 쓰지 마십시오.
>



