# **[technologies-carplay] architecture**

# **Badging**

Apps can display a small red oval containing a white number on their app icon to indicate when new and important information is available.
> 앱 아이콘에 흰색 숫자가 포함된 작은 빨간색 타원을 표시하여 새롭고 중요한 정보를 사용할 수 있음을 나타낼 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Badging_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Badging_2x.png)

**Make badging intuitive.** People should know why your app icon is badged and how to find the related information when they open your app.
> 배깅을 직관적으로 만드십시오. 사람들은 앱 아이콘이 왜 배깅되었는지 그리고 앱을 열 때 관련 정보를 찾는 방법을 알아야 합니다.
>




**Minimize badging.** Don’t overwhelm users by connecting badging with a huge amount of information that changes frequently. Use it to present brief, essential information and atypical content changes that are highly likely to be of interest.
> 배지를 최소화합니다. 배지를 자주 변경되는 엄청난 양의 정보와 연결하여 사용자를 압도하지 마십시오. 이 문서를 사용하여 관심을 가질 가능성이 높은 간략하고 필수적인 정보와 비정형적인 내용 변경사항을 제시합니다.
>




**Draw attention to important information inside your app too.** If you rely solely on app icon badging to highlight information, you run the risk of people missing it. Displaying badges on a tab bar or elsewhere within your app is another way to direct users to important content.
> 앱 내부의 중요한 정보에도 주의를 기울이십시오. 정보를 강조하기 위해 앱 아이콘 배지에만 의존한다면, 사람들이 정보를 놓칠 위험이 있습니다. 앱 내의 탭 바 또는 다른 곳에 배지를 표시하는 것도 중요한 콘텐츠로 사용자를 안내하는 또 다른 방법입니다.
>




**Avoid supplementing badging with alerts.** Even when new or important information is available, users don't want to see an alert the moment they open your app. Instead, make the information discoverable. For related design guidance, see [Error handling](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/architecture#error-handling/) and [Alerts](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/system-elements#alerts).
> 경고로 배지를 보충하지 마십시오. 새로운 정보나 중요한 정보를 사용할 수 있는 경우에도 사용자는 앱을 여는 순간 경고를 보고 싶어하지 않습니다. 대신 정보를 검색할 수 있도록 만드십시오. 관련 설계 지침은 오류 처리 및 경고를 참조하십시오.
>




**Keep badges up to date.** Update your app’s badge as soon as the corresponding information is viewed. You don’t want people to think new or important information is available, only to find that they’ve already seen it.
> 배지를 최신 상태로 유지하십시오. 해당 정보가 표시되는 즉시 앱의 배지를 업데이트하십시오. 여러분은 사람들이 새로운 정보나 중요한 정보를 사용할 수 있다고 생각하지 않기를 원하지만, 그들이 이미 그것을 보았다는 것을 알게 될 뿐입니다.
>




For developer guidance, see [UserNotifications](https://developer.apple.com/documentation/usernotifications).

# **Error handling**

Apps should handle errors gracefully and report them to the user only when absolutely necessary.
> 앱은 반드시 필요한 경우에만 오류를 우아하게 처리하고 사용자에게 보고해야 한다.
>




**Report errors in CarPlay, not on the connected iPhone.** If you must notify the user of a problem, do so clearly in CarPlay. Never direct the user to pick up their iPhone to read or resolve an error.
> 연결된 iPhone이 아닌 CarPlay에서 오류를 보고합니다. 문제를 사용자에게 알려야 할 경우 CarPlay에서 명확하게 보고하십시오. 오류를 읽거나 해결하기 위해 사용자에게 iPhone을 선택하도록 지시하지 마십시오.
>




**Prefer nonintrusive status messages over alerts.** Alerts disrupt the user experience. List error messages inline with content instead of displaying them in alerts.
> 알림보다 침입하지 않는 상태 메시지를 선호합니다. 알림은 사용자 환경을 방해합니다. 오류 메시지를 경고에 표시하는 대신 내용에 맞게 나열합니다.
>




# **Loading**

When content is loading, a blank or static screen can make it seem like your app is frozen, which may cause people to leave your app.
> 콘텐츠를 로드할 때 빈 화면이나 정적 화면을 사용하면 앱이 정지된 것처럼 보일 수 있으며, 이로 인해 사람들이 앱을 떠날 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Loading_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Loading_2x.png)

**Make it clear when loading is occurring.** Consider showing a spinning activity indicator and descriptive text. For related design guidance, see [Activity indicators](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/system-elements#activity-indicators).
> 로딩이 발생할 때는 명확하게 해야 한다. 회전 활동 표시기와 설명 텍스트를 보여주는 것을 고려한다. 관련 설계 지침은 활동 표시기를 참조하십시오.
>




**Show primary content as soon as it's available.** Don’t make people wait for all content to load before seeing the screen they're expecting. Use placeholder text and graphics to identify additional content to come. Replace the placeholder elements as content loads. If possible, preload upcoming content in the background, for example, when the user is listening to audio or navigating a menu.
> 사용 가능한 즉시 기본 콘텐츠를 표시합니다. 사용자가 원하는 화면을 보기 전에 모든 콘텐츠가 로드될 때까지 기다리게 하지 마십시오. 자리 표시자 텍스트 및 그래픽을 사용하여 추가 콘텐츠를 식별합니다. 콘텐츠 로드 시 자리 표시자 요소를 바꿉니다. 가능한 경우, 사용자가 오디오를 듣거나 메뉴를 탐색할 때와 같이 예정된 콘텐츠를 백그라운드에서 미리 로드합니다.
>




# **Navigation**

In CarPlay, there are two main styles of navigation.
> CarPlay에는 크게 두 가지 스타일의 내비게이션이 있습니다.
>




**Flat navigation.** Switch between multiple content categories, typically using a [tab bar](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/system-elements#tab-bars). The Phone app uses this navigation style.
> 평면 탐색. 일반적으로 탭 표시줄을 사용하여 여러 내용 범주 간에 전환할 수 있습니다. 전화 앱은 이 탐색 스타일을 사용합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/NavigationFlat-Graphic_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/NavigationFlat-Graphic_2x.png)

**Hierarchical navigation.** Make one choice per screen until you reach a destination, typically using a [navigation bar](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/system-elements#navigation-bars). To go to another destination, retrace your steps or start over from the beginning and make different choices. The Maps app uses this navigation style.
> 계층 탐색. 일반적으로 탐색 모음을 사용하여 목적지에 도달할 때까지 화면당 하나씩 선택합니다. 다른 목적지로 가기 위해서는, 당신의 발걸음을 다시 따라가거나 처음부터 다시 시작하고 다른 선택을 하세요. 지도 앱은 이 탐색 스타일을 사용합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/NavigationHierarchical-Graphic_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/NavigationHierarchical-Graphic_2x.png)

The Music app implements both flat and hierarchical navigation. At the top level, flat navigation enables switching between your library, your playlists, and radio. As you dive deeper, such as into the albums in your library, content is presented hierarchically.
> 음악 앱은 플랫 및 계층 탐색을 모두 구현합니다. 최상위 수준에서 플랫 탐색을 사용하면 라이브러리, 재생 목록 및 라디오를 전환할 수 있습니다. 라이브러리의 앨범과 같이 더 깊이 들어가면 콘텐츠가 계층적으로 표시됩니다.
>




**Make it fast and easy to get to content.** Structure information to require the least number of taps, swipes, and screens.
> 빠르고 쉽게 컨텐츠에 액세스할 수 있습니다. 최소한의 탭, 스와이프 및 화면이 필요하도록 정보를 구성합니다.
>




**Restore the previous app state when the user returns to your app.** Don't make someone retrace steps to reach their previous location in your app. Preserve and restore your app’s state so the user can continue where they left off. However, avoid resuming audio playback automatically unless it’s the primary feature of your app and is expected by the user.
> 사용자가 앱으로 돌아갈 때 이전 앱 상태를 복원합니다. 다른 사용자가 앱의 이전 위치에 도달하기 위해 단계를 다시 추적하도록 만들지 마십시오. 사용자가 중단한 위치에서 계속할 수 있도록 앱 상태를 보존하고 복원합니다. 그러나 앱의 기본 기능이며 사용자가 원하는 경우가 아니면 오디오 재생을 자동으로 재개하지 마십시오.
>




**In general, provide one path to each screen.** People should always know where they are in your app and how to get to their next destination. Regardless of navigation style, it’s essential that the path through content is logical, predictable, and easy to follow.
> 일반적으로 각 화면에 대한 경로를 하나씩 제공합니다. 사람들은 항상 앱에서 자신이 어디에 있고 다음 목적지로 가는 방법을 알아야 합니다. 탐색 스타일에 관계없이 콘텐츠를 통과하는 경로가 논리적이고 예측 가능하며 따라하기 쉽도록 하는 것이 중요합니다.
>




**When possible, use standard navigation components like tab bars and table views.** Users are already familiar with these controls, and will intuitively know how to get around your app. Audio apps automatically adopt standard navigation controls. See [Audio apps](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/introduction#audio-apps).
> 가능한 경우 탭 표시줄 및 표 보기와 같은 표준 탐색 구성 요소를 사용하십시오. 사용자는 이러한 컨트롤에 이미 익숙하고 직관적으로 앱을 이동하는 방법을 알고 있습니다. 오디오 앱은 자동으로 표준 내비게이션 컨트롤을 채택합니다. 오디오 앱을 참조하십시오.
>




**Use a navigation bar to traverse a hierarchy of data.** The navigation bar’s title can show the current position in the hierarchy, and the back button makes it easy to return to the previous location. For specific guidance, see [Navigation bars](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/system-elements#navigation-bars).
> 탐색 모음을 사용하여 데이터 계층을 이동합니다. 탐색 모음의 제목은 계층에서 현재 위치를 표시할 수 있으며, 뒤로 단추를 누르면 이전 위치로 쉽게 돌아갈 수 있습니다. 자세한 내용은 탐색 모음을 참조하십시오.
>




**Use a tab bar to present peer categories of content or functionality.** A tab bar lets people quickly and easily switch between categories, regardless of the current location. For specific guidance, see [Tab bars](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/system-elements#tab-bars).
> 내용 또는 기능의 피어 범주를 표시하려면 탭 모음을 사용하십시오. 탭 모음을 사용하면 현재 위치에 상관없이 사용자가 쉽고 빠르게 범주 간을 전환할 수 있습니다. 자세한 내용은 탭 모음을 참조하십시오.
>




# **Testing**

Thorough testing is an essential part of designing and building any great app.
> 철저한 테스트는 훌륭한 앱을 설계하고 구축하는 데 필수적인 부분이다.
>




**Test on an actual CarPlay-compatible display, preferably in a car.** Make sure your app is easy to see and navigate from different driver positions, under different weather conditions, and at different times of day.
> 가급적 자동차에서 실제 CarPlay 호환 디스플레이를 테스트하십시오. 앱이 다른 운전자 위치, 다른 날씨 조건 및 다른 시간에 쉽게 보고 탐색할 수 있는지 확인하십시오.
>




**Test with poor network conditions such as while driving through a tunnel and in an area without cellular reception.** Make sure your app handles connection losses and a lack of data gracefully and nonintrusively.
> 터널을 통과하거나 셀룰러 수신이 없는 지역에서 운전하는 것과 같은 열악한 네트워크 조건에서 테스트하십시오. 앱이 연결 손실 및 데이터 부족을 원활하게 처리하는지 확인하십시오.
>




**Test installation and setup.** Install your app on a physical iPhone. Pay close attention to any sign-in requirements and privacy dialogs, and make sure your app appears as expected in CarPlay.
> 설치 및 설정을 테스트합니다. 실제 iPhone에 앱을 설치하십시오. 로그인 요구 사항 및 개인 정보 보호 대화 상자에 주의를 기울이고 CarPlay에서 예상한 대로 앱이 나타나는지 확인하십시오.
>



