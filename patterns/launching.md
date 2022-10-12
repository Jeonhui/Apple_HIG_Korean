# **[patterns] launching**

# People appreciate a streamlined launch experience so they can start using your app or game immediately.
> 사람들은 당신의 앱이나 게임을 즉시 사용할 수 있도록 간소화된 출시 경험을 높이 평가한다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-launching-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-launching-intro-dark_2x.png)

# **Best practices**

**Provide a launch screen if the platform requires it.** In iOS, iPadOS, and tvOS, the system displays a launch screen the moment your app or game starts and quickly replaces it with your first screen, giving people the impression that your experience is fast and responsive. The ideal launch screen is effectively invisible to people, because it simply provides a context for your initial content. watchOS and macOS apps don't need launch screens.
> 플랫폼에 필요한 경우 실행 화면을 제공합니다. iOS, iPadOS 및 tvOS에서는 앱 또는 게임이 시작되는 순간 시스템이 실행 화면을 표시하고 이를 첫 화면으로 빠르게 대체하여 사용자의 경험이 빠르고 반응성이 뛰어나다는 인상을 줍니다. 이상적인 시작 화면은 단순히 초기 콘텐츠에 대한 컨텍스트를 제공하기 때문에 사람들에게 효과적으로 보이지 않습니다. watch OS와 macOS 앱은 시작 화면이 필요하지 않습니다.
>




**Ask for initial setup information only when necessary.** Help people accomplish something as soon as they start your app or game, letting them be successful before you request additional information. As much as possible, get setup information from existing device settings and defaults. If people need to sign in before doing anything useful, consider offering [Sign in with Apple](../technologies/sign-in-with-apple/introduction), or relying on a synchronization service, such as iCloud.
> 초기 설정 정보는 필요한 경우에만 요청하십시오. 사람들이 당신의 앱이나 게임을 시작하자마자 당신이 추가 정보를 요청하기 전에 그들이 성공할 수 있도록 도와준다. 가능한 한 기존 장치 설정 및 기본값에서 설정 정보를 가져옵니다. 사람들이 유용한 일을 하기 전에 로그인해야 한다면 Apple에 로그인하거나 iCloud와 같은 동기화 서비스에 의존하는 것을 고려해 보십시오.
>




**Give people time to start enjoying your app before showing supplementary information, asking for a review, or making permission requests.** At first launch, people want to dive right in; they don’t want to be required to read a lot of content, provide a rating, or grant access to their private data before they get a sense of the experience you offer. To help you streamline first launch, consider:
> 보충 정보를 표시하거나 검토를 요청하거나 사용 권한을 요청하기 전에 다른 사람이 앱을 즐길 수 있는 시간을 줍니다. 처음 시작할 때는 많은 컨텐츠를 읽거나 등급을 제공하거나 개인 데이터에 대한 액세스 권한을 부여하지 않아도 됩니다. 첫 번째 출시를 간소화하기 위해 다음을 고려하십시오.
>




- Letting the App Store display agreements and disclaimers so people can read them before downloading your app
- >  앱 스토어에 동의서 및 거부권을 표시하여 사람들이 앱을 다운로드하기 전에 읽을 수 있도록 함

- Asking for ratings and reviews after people gain enough experience with your app to accurately rate it and provide a substantive review that potential customers might find helpful (for guidance, see [Ratings and reviews](../patterns/ratings-and-reviews))
- >  사람들이 당신의 앱에 대해 정확한 평가를 내리고 잠재 고객이 도움이 될 수 있는 실질적인 리뷰를 제공한 후 평가 및 리뷰를 요청합니다(자세한 내용은 평가 및 리뷰 참조).

- When possible, requesting permission after people indicate that they’re interested in sharing their private data (for guidance, see [Accessing private data](../patterns/accessing-private-data))
- >  가능한 경우 개인 데이터 공유에 관심이 있다고 표시된 후 사용 권한을 요청합니다(자세한 내용은 개인 데이터 액세스 참조).


**Restore the previous state when your app restarts so people can continue where they left off.** Avoid making people retrace steps to reach their previous location in your app or game. Restore granular details of the previous state as much as possible. For example, scroll the view to people’s most recent position, and display windows in the same state and location in which people left them.
> 앱이 다시 시작될 때 이전 상태로 복원하여 사용자가 중단한 위치에서 계속할 수 있습니다. 앱이나 게임의 이전 위치에 도달하기 위한 단계를 다시 추적하지 않도록 합니다. 이전 상태의 세부 정보를 최대한 복원합니다. 예를 들어 보기를 사용자의 가장 최근 위치로 스크롤하고 사용자가 창을 떠난 상태 및 위치에 창을 표시합니다.
>




# **Launch screens**

A launch screen isn’t an onboarding experience or a splash screen, and it isn’t an opportunity for artistic expression. A launch screen’s sole function is to enhance the perception of your experience as quick to launch and immediately ready to use.
> 발사 화면은 탑승 경험이나 스플래시 화면이 아니며 예술적 표현의 기회도 아니다. 실행 화면의 유일한 기능은 실행이 빠르고 즉시 사용할 수 있는 환경에 대한 인식을 향상시키는 것입니다.
>




Not every platform requires a launch screen.
> 모든 플랫폼이 실행 화면을 필요로 하는 것은 아닙니다.
>




- iOS, iPadOS, and tvOS apps must supply a launch screen.
- >  iOS, iPadOS 및 tvOS 앱은 실행 화면을 제공해야 합니다.

- watchOS and macOS apps don’t need a launch screen.
- >  watchOS와 macOS 앱은 실행 화면이 필요하지 않습니다.


**Design a launch screen that’s nearly identical to the first screen of your app.** If you include elements that look different when the app finishes launching, people may experience an unpleasant flash between the launch screen and the first screen of the app. Also make sure that your launch screen matches the device's current appearance, such as [Dark Mode](../foundations/dark-mode).
> 앱의 첫 화면과 거의 동일한 시작 화면을 디자인하십시오. 앱 실행이 끝났을 때 다르게 보이는 요소를 포함하면, 사람들은 실행 화면과 앱의 첫 화면 사이에 불쾌한 플래시를 경험할 수 있다. 또한 실행 화면이 장치의 현재 모양(예: 다크 모드)과 일치하는지 확인합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/patterns/launching/images/launch-screen.png](https://developer.apple.com/design/human-interface-guidelines/patterns/launching/images/launch-screen.png)

Launch screen

![https://developer.apple.com/design/human-interface-guidelines/patterns/launching/images/first-screen.png](https://developer.apple.com/design/human-interface-guidelines/patterns/launching/images/first-screen.png)

First screen

**Avoid including text on your launch screen.** Because the content in a launch screen doesn't change, any text you display won’t be localized.
> 실행 화면에 텍스트를 포함하지 않도록 합니다. 실행 화면의 내용은 변경되지 않으므로 표시되는 텍스트는 지역화되지 않습니다.
>




**Downplay the launch experience.** Design a launch screen that smooths the transition to the first screen of your app or game; avoid designing a launch screen that delays people from immediately getting into the experience.
> 실행 경험을 낮게 평가합니다. 앱이나 게임의 첫 화면으로 원활하게 전환하는 실행 화면을 설계하십시오. 실행 화면을 설계하는 것은 피하십시오.
>




**Don’t advertise.** The launch screen isn’t a branding opportunity. Avoid creating a screen that looks like a splash screen or an "About" window, and don’t include logos or other branding elements unless they’re a fixed part of your app’s first screen. If your game or other immersive app displays a solid color before transitioning to the first screen, create a launch screen that displays only that solid color.
> 광고하지 마세요. 출시 화면은 브랜드화 기회가 아닙니다. 스플래시 화면이나 "정보" 창처럼 보이는 화면은 만들지 말고, 로고나 다른 브랜드 요소는 앱의 첫 화면에서 고정된 부분이 아니면 포함하지 마십시오. 첫 번째 화면으로 전환하기 전에 게임이나 다른 몰입형 앱이 단색을 표시하는 경우 해당 단색만 표시하는 실행 화면을 만듭니다.
>




# **Platform considerations**

*No additional considerations for macOS or watchOS.*
> macOS 또는 워치에 대한 추가 고려 사항 없음OS.
>




# **iOS, iPadOS**

**Launch in the appropriate orientation.** If your app supports both portrait and landscape modes, launch using the device’s current orientation. If your app only runs in one orientation, launch in that orientation and let people rotate the device if necessary. Ensure a landscape-only app responds correctly, regardless of whether people entered landscape orientation by rotating the device left or right. For guidance, see [Layout](../foundations/layout).
> 적절한 방향으로 시작합니다. 앱이 세로 및 가로 모드를 모두 지원하는 경우 장치의 현재 방향을 사용하여 시작합니다. 앱이 한 방향으로만 실행되는 경우 해당 방향으로 시작하고 필요한 경우 사용자가 장치를 회전하도록 합니다. 장치를 왼쪽 또는 오른쪽으로 돌려 가로 방향 전환 여부에 관계없이 가로 방향 전용 앱이 올바르게 응답하는지 확인합니다. 자세한 내용은 레이아웃을 참조하십시오.
>




# **tvOS**

Unlike the [layered images](https://developer.apple.com/design/human-interface-guidelines/foundations/images/#layered-images) throughout much of a tvOS app, the launch screen is static.
> 대부분의 tvOS 앱에서 계층화된 이미지와는 달리, 실행 화면은 정적이다.
>




**In a live-viewing app, consider automatically starting playback soon after people start the app.** People come to your app to watch TV, so you might want to start playing new or recently viewed live content after a few seconds of inactivity. For guidance, see [Live-viewing apps](../patterns/live-viewing-apps).
> 실시간 보기 앱에서 사용자가 앱을 시작한 후 바로 자동으로 재생을 시작하는 것을 고려하십시오. 사람들은 TV를 보기 위해 당신의 앱에 오기 때문에, 당신은 몇 초 동안 활동을 하지 않은 후에 새로운 또는 최근에 본 라이브 콘텐츠를 재생하기를 원할 수도 있다. 자세한 내용은 실시간 보기 앱을 참조하십시오.
>



