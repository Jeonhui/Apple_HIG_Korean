# **[inputs] pointing-devices**

## People can use pointing devices like a trackpad or mouse to supplement touchscreen and keyboard input, letting them use clicks and fluid, intuitive gestures to initiate actions.
> 트랙패드나 마우스와 같은 포인팅 장치를 사용하여 터치스크린과 키보드 입력을 보완하여 클릭과 유동적이고 직관적인 제스처를 사용하여 작업을 시작할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-pointing-devices-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-pointing-devices-intro_2x.png)

People appreciate the precision and flexibility that pointing devices offer. iPadOS builds on the traditional pointer experience, automatically adapting the pointer to the current context and providing rich visual feedback at a level of precision that enhances productivity and simplifies common tasks on a touchscreen device. The iPadOS pointing system gives people an additional way to interact with apps and content — it doesn’t replace touch.
> 사람들은 포인팅 장치가 제공하는 정밀도와 유연성을 높이 평가합니다. iPadOS는 포인터를 현재 컨텍스트에 자동으로 적용하고 터치스크린 장치에서 일반적인 작업을 단순화하는 정밀도 수준에서 풍부한 시각적 피드백을 제공하는 전통적인 포인터 경험을 기반으로 합니다. 아이패드OS 포인팅 시스템은 사람들에게 터치를 대체하지 않고 앱 및 콘텐츠와 상호 작용할 수 있는 추가적인 방법을 제공합니다.
>




On iPad, some people may continue to use touch only, whereas others may prefer to use the pointer or a combination of both. On a Mac, people typically use a mouse or trackpad to control the pointer, although many people prefer to use the keyboard to do so.
> 아이패드에서 어떤 사람들은 터치만 계속해서 사용하는 반면, 다른 사람들은 포인터나 둘의 조합을 사용하는 것을 선호할 수 있다. Mac에서는 일반적으로 마우스나 트랙패드를 사용하여 포인터를 제어하지만, 많은 사람들이 키보드를 사용하여 포인터를 제어하는 것을 선호합니다.
>




# **Best practices**

**Be consistent when responding to mouse and trackpad gestures.**People expect most gestures to work the same throughout the system, regardless of the app or game they’re using. On a Mac, for example, people rely on the “Swipe between pages” gesture to behave the same way whether they’re browsing individual document pages, webpages, or images.
> 마우스 및 트랙패드 제스처에 응답할 때 일관성을 유지합니다.사람들은 그들이 사용하는 앱이나 게임에 관계없이 대부분의 제스처가 시스템 전체에서 동일하게 작동하기를 기대한다. 예를 들어 Mac에서는 "페이지 간 전환" 제스처를 사용하여 개별 문서 페이지, 웹 페이지 또는 이미지를 검색할 때와 동일한 방식으로 동작합니다.
>




**Avoid redefining systemwide trackpad gestures.** Even in a game that uses app-specific gestures in a custom way, people expect systemwide gestures to be available for actions like revealing the Dock or Mission Control. Remember that Mac users can customize the gestures for performing systemwide actions.
> 시스템 전체의 트랙패드 제스처를 재정의하지 마십시오. 앱별 제스처를 사용자 지정 방식으로 사용하는 게임에서도 도킹 또는 미션 컨트롤을 표시하는 등의 작업에 시스템 전체의 제스처를 사용할 수 있기를 기대합니다. Mac 사용자는 시스템 전체 작업을 수행하기 위한 제스처를 사용자 지정할 수 있습니다.
>




**Provide a consistent experience in your iPadOS app, whether people are using touchscreen gestures, a pointing device, or a keyboard.** On their iPad, people tend to move fluidly between using touch and a connected input device, and they don’t want to learn different interactions for each mode or for each app they use.
> iPad에서는 터치스크린 제스처, 포인팅 장치 또는 키보드를 사용하는 경우에도 iPad OS 앱에서 일관된 경험을 제공합니다. iPad에서는 터치와 연결된 입력 장치 사이를 유동적으로 이동하는 경향이 있으며 각 모드 또는 사용하는 앱에 대해 서로 다른 상호 작용을 배우고 싶어하지 않습니다.
>




**Let people use the pointer to reveal and hide controls that automatically minimize or fade out.** In iPadOS, for example, people can reveal the minimized Safari toolbar by holding the pointer over it (the toolbar minimizes again when the pointer moves away). People can also move the pointer to reveal or hide playback controls while they watch a full-screen video.
> 예를 들어, iPadOS에서 사용자는 포인터를 사용하여 자동으로 최소화하거나 페이드아웃하는 컨트롤을 표시하거나 숨길 수 있습니다. 또한 사용자는 전체 화면 비디오를 보는 동안 재생 컨트롤을 표시하거나 숨길 수 있습니다.
>




**Enable a consistent experience when people press and hold a modifier key while interacting with objects in your app.** For example, if people can duplicate an object by pressing and holding the Option key while they drag that object, ensure the result is the same whether they drag using touch or the pointer.
> 사용자가 앱에서 개체와 상호 작용하는 동안 수정자 키를 길게 누를 때 일관된 환경을 사용할 수 있습니다. 예를 들어, 사용자가 개체를 끌 때 옵션 키를 길게 눌러 개체를 복제할 수 있는 경우 터치를 사용하든 포인터를 사용하여 끌든 결과가 동일한지 확인하십시오.
>




# **Platform considerations**

*No additional considerations for iOS. Not supported in tvOS or watchOS.*
> iOS에 대한 추가 고려 사항은 없습니다. TVOS 또는 워치에서 지원되지 않음운영 체제
>




# **iPadOS**

