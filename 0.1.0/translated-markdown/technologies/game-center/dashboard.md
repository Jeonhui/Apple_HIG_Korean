# **[technologies-game-center] dashboard**

After players have signed into Game Center, they can launch the in-game dashboard by selecting the access point within your game. The dashboard is a full-screen view that appears on top of your game and gives players access to their Game Center profile and information.
> 플레이어가 게임 센터에 로그인한 후 게임 내 액세스 지점을 선택하여 게임 내 대시보드를 시작할 수 있습니다. 대시보드는 게임 위에 나타나는 전체 화면 보기로, 플레이어가 게임 센터 프로필 및 정보에 액세스할 수 있도록 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/game-center-dashboard_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/game-center-dashboard_2x.png)

The dashboard — like the access point and other Game Center UI — uses a background material that adapts to the appearance of your game. The translucency of this material provides a sense of depth and helps remind players that they haven’t left your game.
> 대시보드는 액세스 지점 및 기타 Game Center UI와 마찬가지로 게임의 모양에 맞는 배경 자료를 사용합니다. 이 자료의 투명성은 깊이감을 제공하고 플레이어에게 게임에서 떠나지 않았음을 상기시키는 데 도움이 됩니다.
>




**Pause your game while the dashboard is present.** Pausing your game helps you avoid potential performance impacts, but it also helps players focus on their Game Center information without feeling that the game is continuing without them.
> 대시보드가 있는 동안 게임을 일시 중지합니다. 게임을 일시 중지하면 잠재적인 성능 저하를 방지할 수 있지만 플레이어가 게임이 없는 상태에서 게임 센터 정보에 집중할 수 있습니다.
>




If necessary, your game can include custom links that open the dashboard or take players directly to their Game Center profile. For guidance, see [Custom dashboard links](../technologies/game-center/custom-dashboard-links).
> 필요한 경우 게임에 대시보드를 열거나 플레이어를 게임 센터 프로필로 직접 이동하는 사용자 지정 링크를 포함할 수 있습니다. 자세한 내용은 사용자 지정 대시보드 링크를 참조하십시오.
>




# **Creating a dashboard image (tvOS)**
> 대시보드 이미지 생성(tvOS)
>




Games that run in tvOS can display an optional image at the top of the in-game dashboard.
> TVOS에서 실행되는 게임은 게임 내 대시보드 상단에 옵션 이미지를 표시할 수 있다.
>




**Use a simple, easily recognizable image that looks great at a distance.** Although you should avoid using your app icon for this image, you could use your game’s logo or word mark. To ensure that your image contrasts well with the dashboard appearance, consider using transparency to let the dashboard background to show through.
> 멀리서도 쉽게 알아볼 수 있는 단순한 이미지를 사용하십시오. 이 이미지에 앱 아이콘을 사용하는 것은 피해야 하지만 게임의 로고나 단어 표시를 사용할 수 있습니다. 이미지가 대시보드 모양과 잘 대비되도록 하려면 투명도를 사용하여 대시보드 배경이 보이도록 하십시오.
>




Use the following specifications to create a dashboard image.
> 다음 사양을 사용하여 대시보드 이미지를 생성할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/tvos-dashboard-image_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/game-center/images/tvos-dashboard-image_2x.png)

| Attribute | Value |
| --- | --- |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 600x180 pt (1200x360 px @2x) |

Custom dashboard artwork is not focusable.
> 사용자 지정 대시보드 아트워크는 초점을 맞출 수 없습니다.
>



