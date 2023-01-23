# **[technologies-game-center] achievements**

Achievements can give players added incentive to stay engaged with your game. In iOS 14 and later, Game Center achievements appear in a collectible card format that highlights the player’s progress and showcases your artwork. Achievements are a prominent feature in Game Center UI, so it’s essential to design beautiful, high-quality assets that catch the eye and encourage players to return to your game.
> 성과를 통해 플레이어는 게임에 참여할 수 있는 추가 인센티브를 얻을 수 있습니다. iOS 14 이상에서는 게임 센터 성과가 플레이어의 진행 상황을 강조하고 아트워크를 보여주는 수집 가능한 카드 형식으로 나타납니다. 성과는 게임 센터 UI의 주요 기능이므로 눈에 띄는 아름답고 고품질의 자산을 설계하고 플레이어가 게임에 복귀하도록 장려하는 것이 중요합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/achievements-grouped_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/achievements-grouped_2x.png)

If necessary, your game can include a custom link that takes players directly to the achievements area in the dashboard. For guidance, see [Custom dashboard links](../technologies/game-center/custom-dashboard-links).
> 필요한 경우 게임에 대시보드의 성과 영역으로 직접 이동하는 사용자 지정 링크가 포함될 수 있습니다. 자세한 내용은 사용자 지정 대시보드 링크를 참조하십시오.
>




# **Integrating your achievements into Game Center**
> 성과를 Game Center에 통합
>




Game Center defines four achievement states: locked, in-progress, hidden, and completed. The system groups achievements by completion status, displaying completed achievements in the Completed group and all other achievements in the Locked group.
> 게임 센터는 잠금, 진행 중, 숨김, 완료의 네 가지 달성 상태를 정의합니다. 시스템은 완료 상태별로 성과를 그룹화하여 완료된 성과를 완료된 그룹에 표시하고 잠금 그룹에 있는 다른 모든 성과를 표시합니다.
>




**Align your achievement types with Game Center achievement states.** The system displays achievements differently, depending on state. For example, an in-progress achievement includes a percentage value that shows how close players are to completion, whereas a locked achievement displays a padlock glyph. When you map your achievements to the four Game Center achievement states, you give players a consistent experience and you help them see at a glance the types of achievements your game offers.
> 성취 유형을 게임 센터 성취 상태에 맞춰 조정합니다. 시스템은 성취도를 상태에 따라 다르게 표시합니다. 예를 들어, 진행 중인 성과에는 플레이어가 완료에 얼마나 근접했는지 보여주는 백분율 값이 포함되어 있는 반면, 잠긴 성과에는 자물쇠 모양의 글리프가 표시됩니다. 네 가지 게임 센터 성취 상태에 자신의 성취도를 매핑하면 플레이어에게 일관된 경험을 제공하고 게임이 제공하는 성취 유형을 한 눈에 볼 수 있도록 도와줍니다.
>




**Determine a display order for your achievements.** The order in which you upload achievements is the order in which they’re displayed. For example, you might want your achievements to appear in an order that corresponds to the most common path through your game.
> 성과의 표시 순서를 결정합니다. 성과를 업로드하는 순서는 성과가 표시되는 순서입니다. 예를 들어, 게임의 가장 일반적인 경로에 해당하는 순서로 성과를 표시할 수 있습니다.
>




# **Creating great achievement images**

When players complete an achievement, the system moves the card that represents it into the Completed group, fills the card’s circular frame with your artwork, and adds a badge that displays the completion date. Achievement artwork is required when you adopt Game Center achievements.
> 플레이어가 성과를 완료하면 시스템은 이를 나타내는 카드를 완료 그룹으로 이동하고 카드의 원형 프레임을 사용자의 아트워크로 채우고 완료 날짜를 표시하는 배지를 추가합니다. 게임 센터 성과물을 채택할 때 성과물 아트워크가 필요합니다.
>




**Design rich, high-quality images that complement your game and make players feel rewarded.** Providing beautiful achievements that reward a variety of gameplay styles and skill levels can encourage players to stay engaged with your game and earn more achievements. Because players appreciate earning unique achievements that remind them of each accomplishment, avoid reusing the same asset to represent more than one achievement. If you don’t provide an asset for an achievement, the card shows a placeholder image instead.
> 게임을 보완하고 플레이어에게 보상을 주는 풍부한 고품질 이미지를 디자인하십시오. 다양한 게임 플레이 스타일과 기술 수준에 보상을 주는 아름다운 성과를 제공하면 플레이어가 게임에 계속 참여하고 더 많은 성과를 얻을 수 있습니다. 참가자들은 각각의 성취를 상기시키는 독특한 성취를 얻는 것을 좋아하기 때문에, 하나 이상의 성취를 나타내기 위해 동일한 자산을 재사용하는 것을 피하라. 성과에 대한 자산을 제공하지 않으면 카드에 자리 표시자 이미지가 대신 표시됩니다.
>




**Design a centered image for each achievement.** The system applies a circular mask to your achievement image, so be sure to keep primary content centered.
> 각 성취도에 대한 중심 이미지를 설계합니다. 시스템은 성취도 이미지에 원형 마스크를 적용하므로, 기본 콘텐츠를 중심으로 유지해야 합니다.
>




**Create achievement images in the appropriate size and format.** Use the following specifications to create opaque images for games that run in iOS, iPadOS, and macOS.
> iOS, iPadOS 및 macOS에서 실행되는 게임용 불투명 이미지를 만들려면 다음 사양을 사용하십시오.
>




| Attribute | Value |
| --- | --- |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 512x512 pt (1024x1024 px @2x) |
| Mask diameter | 512 pt (1024 px @2x) |

Use the following specifications to create an achievement image.
> 다음 사양을 사용하여 성과 이미지를 만듭니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/tvos-achievement-image-layout_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/tvos-achievement-image-layout_2x.png)

| Attribute | Value |
| --- | --- |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 320x320 pt (640x640 px @2x) |
| Mask diameter | 200 pt (400 px @2x) |

In tvOS, achievement images aren’t focusable.
> TVOS에서는 성과 이미지에 초점을 맞출 수 없습니다.
>




# **Writing text that describes your achievements**
> 성과를 설명하는 텍스트 작성
>




Regardless of an achievement’s state, the card displays your title and description below the circular frame.
> 성과의 상태에 관계없이, 카드는 원형 프레임 아래에 귀하의 제목과 설명을 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/achievement_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/achievement_2x.png)

**Be succinct.** The achievement card limits the title and description to two lines each. If your title or description wraps beyond two lines, the card truncates the text.
> 간결하게 하세요. 성취 카드는 제목과 설명을 각각 두 줄로 제한합니다. 제목이나 설명이 두 줄을 넘으면 카드가 텍스트를 잘라냅니다.
>




**Use correct capitalization styles.** In particular, avoid using all capital letters in your title and description. The achievement title should use title-style capitalization and the description should use sentence-style.
> 올바른 대문자 스타일을 사용하십시오. 특히 제목과 설명에 모두 대문자를 사용하지 마십시오. 성과 제목은 제목 스타일 대문자를 사용하고 설명은 문장 스타일을 사용해야 합니다.
>




**Be creative with an achievement’s title, but straightforward with its description.** Although most players appreciate entertaining titles, they expect an achievement’s description to specify how to earn it.
> 성취의 제목을 가지고 창의적이 되되, 그 묘사를 솔직하게 하라. 비록 대부분의 선수들이 재미있는 타이틀을 높이 평가하지만, 그들은 성취의 묘사가 그것을 얻는 방법을 명시하기를 기대한다.
>



