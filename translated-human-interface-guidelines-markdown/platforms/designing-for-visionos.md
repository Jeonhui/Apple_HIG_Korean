### [[Platforms](./translated-human-interface-guidelines-markdown/platforms.md)]  
  
# **Designing for visionOS**  

=========================



When people wear Apple Vision Pro, they enter an infinite 3D space where they can engage with your app or game while staying connected to their surroundings.  

> 사람들이 Apple Vision Pro를 착용하면 주변 환경에 연결된 상태로 앱이나 게임에 참여할 수 있는 무한한 3D 공간에 들어갑니다.
>

![A stylized representation of Apple Vision Pro shown on top of a grid. The image is overlaid with rectangular and circular grid lines and is tinted green to subtly reflect the green in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/df20c2f5927e27ce269d973c6adb3b43/platforms-visionOS-intro@2x.png)



As you begin designing your app or game for visionOS, start by understanding the fundamental device characteristics and patterns that distinguish the platform. Use these characteristics and patterns to inform your design decisions and help you create immersive and engaging experiences.  

As you begin designing your app or game for visionOS, start by understanding the fundamental device characteristics and patterns that distinguish the platform. Use these characteristics and patterns to inform your design decisions and help you create immersive and engaging experiences.  





**Space.** Apple Vision Pro offers a limitless canvas where people can view virtual content like   

![A stylized representation of Apple Vision Pro shown on top of a grid. The image is overlaid with rectangular and circular grid lines and is tinted green to subtly reflect the green in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/df20c2f5927e27ce269d973c6adb3b43/platforms-visionOS-intro@2x.png)



As you begin designing your app or game for visionOS, start by understanding the fundamental device characteristics and patterns that distinguish the platform. Use these characteristics and patterns to inform your design decisions and help you create immersive and engaging experiences.  

> 비전을 위한 앱 또는 게임 설계를 시작할 때OS는 플랫폼을 구별하는 기본적인 장치 특성과 패턴을 이해하는 것부터 시작한다. 이러한 특성과 패턴을 사용하여 설계 결정을 알리고 몰입적이고 매력적인 경험을 만들 수 있습니다.
>





**Space.** Apple Vision Pro offers a limitless canvas where people can view virtual content like   

> **공간.** Apple Vision Pro는 다음과 같은 가상 콘텐츠를 볼 수 있는 무제한 캔버스를 제공합니다
>

[windows](/design/human-interface-guidelines/windows)

,   

[volumes](/design/human-interface-guidelines/windows#Volumes)

, and 3D objects, and choose to enter deeply immersive experiences that can transport them to different places.  

> , 그리고 3D 물체를 다른 장소로 운반할 수 있는 깊이 있는 몰입감 있는 경험을 입력하도록 선택합니다.
>





**Immersion.** In a visionOS app, people can fluidly transition between different levels of   

> **몰입.** 환상 속에서OS 앱을 사용하면 다양한 레벨 간에 유동적으로 전환할 수 있습니다
>

[immersion](/design/human-interface-guidelines/immersive-experiences)

. By default, an app launches in the   

> . 기본적으로 앱은 다음에서 시작됩니다
>

*Shared Space* where multiple apps can run side-by-side and people can open, close, and relocate windows. People can also choose to transition an app to a   

> 여러 앱을 나란히 실행하고 사람들이 창을 열고 닫고 재배치할 수 있는 *공유 공간*. 사람들은 또한 앱을 a로 전환하도록 선택할 수 있다
>

*Full Space*, where it’s the only app running. While in a Full Space app, people can view 3D content blended with their surroundings, open a portal to view another place, or enter a different world.  

> *Full Space*. 유일한 앱을 실행할 수 있습니다. Full Space 앱에서 사용자는 주변 환경과 혼합된 3D 콘텐츠를 보거나 포털을 열어 다른 장소를 보거나 다른 세계로 들어갈 수 있습니다.
>





**Passthrough.**   

[Passthrough](/design/human-interface-guidelines/immersive-experiences#Immersion-and-passthrough)

 provides live video from the device’s external cameras, and helps people interact with virtual content while also seeing their actual surroundings. When people want to see more or less of their surroundings, they use the   

> 는 장치의 외부 카메라에서 라이브 비디오를 제공하며 사람들이 실제 환경을 보는 동시에 가상 콘텐츠와 상호 작용할 수 있도록 도와줍니다. 사람들이 그들의 주변을 더 많이 혹은 덜 보고 싶을 때, 그들은 사용한다
>

[Digital Crown](/design/human-interface-guidelines/digital-crown)

 to control the amount of passthrough.  

> 패스스루의 양을 제어합니다.
>





**Spatial Audio.** Vision Pro combines acoustic and visual-sensing technologies to model the sonic characteristics of a person’s surroundings, automatically making audio sound natural in their space. When an app receives a person’s permission to access information about their surroundings, it can fine-tune   

> **공간 오디오.** Vision Pro는 음향 및 시각 감지 기술을 결합하여 사람의 주변 환경의 음향 특성을 모델링하여 자동으로 공간에서 오디오 소리를 자연스럽게 만듭니다. 앱이 사용자의 주변 정보 접근 권한을 받으면 미세 조정할 수 있다
>

[Spatial Audio](/design/human-interface-guidelines/playing-audio#visionOS)

 to bring custom experiences to life.  

> 사용자 정의 경험을 되살리기 위한 것입니다.
>





**Focus and gestures.** In general, people interact with Vision Pro using their   

> **집중과 몸짓.** 일반적으로, 사람들은 Vision Pro와 상호작용한다
>

[eyes](/design/human-interface-guidelines/eyes)

 and   

[hands](/design/human-interface-guidelines/gestures#visionOS)

. People perform most actions by looking at a virtual object to bring   

> . 사람들은 가져올 가상 객체를 보고 대부분의 작업을 수행합니다
>

[focus](/design/human-interface-guidelines/focus-and-selection)

 to it and making an   

> 그것을 하고 그것을 만든다
>

*indirect gesture*, like a tap, to activate it. People can also use a   

> 탭과 같은 *잠금 동작*을 활성화합니다. 사람들은 또한 사용할 수 있다
>

*direct gesture* to interact with a virtual object by touching it with a finger.  

> *직접 제스처*를 사용하여 가상 개체와 상호 작용할 수 있습니다.
>





**Ergonomics.** While wearing Vision Pro, people rely entirely on the device’s cameras for everything they see, both real and virtual, so maintaining visual comfort is paramount. The system helps maintain comfort by automatically placing content so it’s relative to the wearer’s head, regardless of the person’s height or whether they’re sitting, standing, or lying down. Because visionOS brings content to people — instead of making people move to reach the content — people can remain at rest while engaging with apps and games.  

> **경제학.** Vision Pro를 착용하는 동안 사람들은 실제와 가상 모두에서 보이는 모든 것을 기기의 카메라에 전적으로 의존하므로 시각적 편안함을 유지하는 것이 무엇보다 중요합니다. 이 시스템은 자동으로 콘텐츠를 배치함으로써 편안함을 유지하는 데 도움을 주어 사람의 키나 앉거나 서 있거나 누워 있거나 상관없이 착용자의 머리에 상대적으로 콘텐츠를 배치합니다. 왜냐하면 시력이OS는 사람들에게 컨텐츠를 제공합니다. 사람들이 컨텐츠에 도달하기 위해 이동하는 대신, 사람들은 앱과 게임에 참여하면서 안정을 유지할 수 있습니다.
>





**Accessibility.** Apple Vision Pro supports   

> **접근성.** Apple Vision Pro 지원
>

[accessibility](/design/human-interface-guidelines/accessibility)

 technologies like VoiceOver, Switch Control, Dwell Control, Guided Access, Head Pointer, and many more, so people can use the interactions that work for them. In visionOS, as in all platforms, system-provided UI components build in accessibility support by default, while system frameworks give you ways to enhance the accessibility of your app or game.  

> VoiceOver, 스위치 제어, 드웰 제어, Guided Access, Head Pointer 등과 같은 기술을 사용하여 사람들이 상호 작용을 사용할 수 있습니다. 시야에OS는 모든 플랫폼과 마찬가지로 시스템에서 제공하는 UI 구성 요소가 기본적으로 접근성을 지원하며, 시스템 프레임워크는 앱이나 게임의 접근성을 향상시키는 방법을 제공합니다.
>





[Best practices](/design/human-interface-guidelines/designing-for-visionos#Best-practices)

------------------------------------------------------------------------------------------



Great visionOS apps and games are approachable and familiar, while offering extraordinary experiences that can surround people with beautiful content, expanded capabilities, and captivating adventures.  

> 시력이 좋다OS 앱과 게임은 접근하기 쉽고 친숙한 반면, 아름다운 콘텐츠, 확장된 기능, 매혹적인 모험으로 사람들을 둘러쌀 수 있는 특별한 경험을 제공한다.
>





**Embrace the unique features of Apple Vision Pro.** Take advantage of space, Spatial Audio, and immersion to bring life to your experiences, while integrating passthrough, focus, and gestures in ways that feel at home on the device.  

> **Apple Vision Pro의 고유한 기능을 활용하십시오.** 공간, 공간 오디오 및 몰입을 활용하여 경험에 생기를 불어넣는 동시에 패스스루, 포커스 및 제스처를 장치에서 편안하게 느낄 수 있습니다.
>





**Consider the entire spectrum of immersion as you design ways to present your app’s most distinctive moments.** You can present experiences in a windowed, UI-centric context, a fully immersive context, or something in between. For each key moment in your app, find the minimum level of immersion that suits it best — don’t assume that every moment needs to be fully immersive.  

> **앱의 가장 독특한 순간을 표현하는 방법을 설계할 때 전체 몰입 범위를 고려하십시오.** 당신은 윈도우, UI 중심의 컨텍스트, 완전히 몰입된 컨텍스트 또는 그 사이의 무언가에서 경험을 제시할 수 있다. 앱의 각 주요 순간에 가장 적합한 최소 몰입 수준을 찾으십시오. 모든 순간이 완전히 몰입되어야 한다고 가정하지 마십시오.
>





**Use windows for contained, UI-centric experiences.** To help people perform standard tasks, prefer standard   

> **컨테이너된 UI 중심의 경험을 위해 창을 사용합니다.** 사람들이 표준 작업을 수행하는 데 도움이 되도록 표준 작업을 선호합니다
>

[windows](/design/human-interface-guidelines/windows#visionOS)

 that appear as planes in space and contain familiar controls. In visionOS, people can relocate windows anywhere they want, and the system’s   

> 공간에 평면으로 나타나고 친숙한 컨트롤을 포함합니다. 시야에OS, 사용자는 원하는 위치에 창을 재배치할 수 있으며 시스템은
>

[dynamic scaling](/design/human-interface-guidelines/spatial-layout#Scale)

 helps keep window content legible whether it’s near or far.  

> 창 내용을 가까운 곳이든 먼 곳이든 쉽게 읽을 수 있도록 합니다.
>





**Prioritize comfort.** To help people stay comfortable and physically relaxed as they interact with your app or game, keep the following fundamentals in mind.  

> **편안함을 우선시합니다.** 사람들이 당신의 앱이나 게임과 상호 작용할 때 편안하고 신체적으로 편안한 상태를 유지할 수 있도록 다음과 같은 기본 사항을 염두에 두십시오.
>





* Display content within a person’s   

> * 사용자의 웹 페이지 내 내용 표시
>

[field of view](/design/human-interface-guidelines/spatial-layout#Field-of-view)

, positioning it relative to their head. Avoid placing content in places where people have to turn their head or change their position to interact with it.

> , 그들의 머리에 상대적으로 위치시키는 것. 사람들이 콘텐츠와 상호 작용하기 위해 고개를 돌리거나 위치를 변경해야 하는 장소에 콘텐츠를 배치하지 마십시오.
>

* Avoid displaying   

[motion](/design/human-interface-guidelines/motion#visionOS)

 that’s overwhelming, jarring, too fast, or missing a stationary frame of reference.

> 그것은 압도적이고, 거슬리고, 너무 빠르며, 고정된 기준 프레임을 놓치는 것이다.
>

* Support   

[indirect gestures](/design/human-interface-guidelines/gestures#visionOS)

 that let people interact with apps while their hands rest in their lap or at their sides.

> 사람들이 그들의 손이 무릎이나 옆구리에 있는 동안 앱과 상호 작용할 수 있도록 한다.
>

* If you support direct gestures, make sure the interactive content isn’t too far away and that people don’t need to interact with it for extended periods.

> * 직접 제스처를 지원하는 경우 대화형 콘텐츠가 너무 멀리 있지 않은지, 사람들이 장시간 동안 콘텐츠와 상호 작용할 필요가 없는지 확인하십시오.
>

* Avoid encouraging people to move too much while they’re in a fully   

> * 사람들이 완전히 있는 동안 너무 많이 움직이게 하는 것을 피하세요
>

[immersive experience](/design/human-interface-guidelines/immersive-experiences)

.



**Help people share activities with others.** When you use   

> **사람들이 다른 사람들과 활동을 공유할 수 있도록 도와줍니다.** 사용할 때
>

[SharePlay](/design/human-interface-guidelines/shareplay#visionOS)

 to support shared activities, people can view the   

> 공유 활동을 지원하기 위해, 사람들은 볼 수 있다
>

*Spatial Personas* of other participants, making it feel like everyone is together in the same space.  

> 다른 참가자들의 *공간적 인물*로, 모든 사람이 같은 공간에 함께 있는 것처럼 느끼게 합니다.
>





[Resources](/design/human-interface-guidelines/designing-for-visionos#Resources)

--------------------------------------------------------------------------------



#### [Related](/design/human-interface-guidelines/designing-for-visionos#Related)



[Apple Design Resources](https://developer.apple.com/design/resources/#visionOS-apps)





#### [Developer documentation](/design/human-interface-guidelines/designing-for-visionos#Developer-documentation)



[Creating your first visionOS app](/documentation/visionOS/creating-your-first-visionos-app)





#### [Videos](/design/human-interface-guidelines/designing-for-visionos#Videos)



[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/15489B11-8744-483D-AD38-EF78D8962FF4/8126_wide_250x141_1x.jpg) Principles of spatial design](https://developer.apple.com/videos/play/wwdc2023/10072)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/C6CDCC79-CCD0-4D2F-A4D1-8FC70DC663DB/8127_wide_250x141_1x.jpg) Design for spatial input](https://developer.apple.com/videos/play/wwdc2023/10073)

[![](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/38E4EE32-29B5-4478-B8B6-35B8ACA67B16/8130_wide_250x141_1x.jpg) Design for spatial user interfaces](https://developer.apple.com/videos/play/wwdc2023/10076)

[Change log](/design/human-interface-guidelines/designing-for-visionos#Change-log)

----------------------------------------------------------------------------------
