# **[technologies] augmented-reality**

# Augmented reality (or AR) lets you deliver immersive, engaging experiences that seamlessly blend virtual objects with the real world.
> 증강 현실(또는 AR)은 가상 물체를 실제 세계와 원활하게 혼합하는 몰입감 있고 매력적인 경험을 제공할 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-augmented-reality-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-augmented-reality-intro_2x.png)

Using the device's camera to present the physical world onscreen live, your app superimposes three-dimensional virtual objects, creating the illusion that these objects actually exist. Depending on the experiences your app offers, people can reorient the device to explore the objects from different angles, interact with objects using gestures and movement, and even join other people in multiuser AR experiences. For developer guidance, see [ARKit](https://developer.apple.com/documentation/arkit).
> 장치의 카메라를 사용하여 물리적 세계를 화면에 라이브로 표시하면, 앱은 3차원 가상 물체를 중첩하여 이러한 물체가 실제로 존재하는 것 같은 착각을 일으킨다. 당신의 앱이 제공하는 경험에 따라, 사람들은 다른 각도에서 물체를 탐색하고, 제스처와 움직임을 사용하여 물체와 상호 작용하며, 심지어 다중 사용자 AR 경험에 다른 사람들과 함께 할 수 있다. 개발자 지침은 ARKit를 참조하십시오.
>




**Offer AR features only on capable devices.** If your app's primary purpose is AR, make your app available only to devices that support ARKit. If your app includes features that require specific AR capabilities, or if AR features are optional in your app, don’t show people an error if they try to use these features on a device that doesn’t support them; instead, simply avoid offering the feature on an unsupported device. For developer guidance, see [Verifying device support and user permission](https://developer.apple.com/documentation/arkit/verifying_device_support_and_user_permission).
> AR 기능을 제공할 수 있는 장치에만 AR 기능을 제공합니다. 앱의 주요 목적이 AR이라면 ARKit를 지원하는 장치에만 사용할 수 있습니다. 특정 AR 기능이 필요한 기능이 앱에 포함되어 있거나 AR 기능이 앱에서 선택 사항인 경우, 사용자가 해당 기능을 지원하지 않는 장치에서 이러한 기능을 사용하려고 하면 오류를 표시하지 말고, 지원되지 않는 장치에서 해당 기능을 제공하지 않도록 하십시오. 개발자 지침은 장치 지원 및 사용자 권한 확인을 참조하십시오.
>




# **Creating an engaging, comfortable experience**
> 매력적이고 편안한 환경 만들기
>




**Let people use the entire display.** Devote as much of the screen as possible to displaying the physical world and your app's virtual objects. Avoid cluttering the screen with controls and information that diminish the immersive experience.
> 사람들이 전체 디스플레이를 사용할 수 있도록 합니다. 가능한 한 많은 화면을 물리적 세계와 앱의 가상 개체를 표시하는 데 할애하십시오. 몰입감을 떨어뜨리는 컨트롤과 정보로 화면을 어지럽게 하지 마십시오.
>




**Strive for convincing illusions when placing realistic objects.** Design detailed 3D assets with lifelike textures to create objects that appear to inhabit the physical environment in which you place them. Using information from ARKit, you can scale objects properly and position them on detected real-world surfaces, reflect environmental lighting conditions and simulate camera grain, cast top-down diffuse object shadows on real-world surfaces, and update visuals as the camera's position changes. To help avoid breaking the illusion you create, make sure your app updates scenes 60 times per second so objects don’t appear to jump or flicker.
> 현실적인 물체를 배치할 때 설득력 있는 환상을 위해 노력하십시오. 실제와 같은 질감으로 세부적인 3D 자산을 설계하여 물체를 배치한 물리적 환경에 상주하는 것처럼 보이는 물체를 만드십시오. ARKit의 정보를 사용하면 물체의 크기를 적절하게 조정하여 감지된 실제 표면에 배치하고, 환경 조명 조건을 반영하고 카메라 입자를 시뮬레이션하며, 실제 표면에 하향식 확산 물체 그림자를 캐스팅하고, 카메라의 위치가 변경되면 시각 자료를 업데이트할 수 있습니다. 사용자가 만든 환상을 깨는 것을 방지하려면 앱이 초당 60회 장면을 업데이트하여 물체가 점프하거나 깜박이는 것처럼 보이지 않도록 하십시오.
>




**Consider how virtual objects with reflective surfaces show the environment.** Reflections in ARKit are approximations based on the environment captured by the camera. To help maintain the illusion that an AR experience is real, prefer small or coarse reflective surfaces that downplay the effect of these approximations.
> 반사 표면이 있는 가상 물체가 환경을 어떻게 보여주는지 생각해보세요. ARK에서의 반사는 카메라가 포착한 환경을 기반으로 한 근사치입니다. AR 경험이 실제라는 환상을 유지하는 데 도움이 되도록 이러한 근사치의 효과를 경시하는 작고 거친 반사 표면을 선호한다.
>




**Use audio and haptics to enhance the immersive experience.** A sound effect or bump sensation is a great way to confirm that a virtual object has made contact with a physical surface or other virtual object. Background music can also help envelop people in the virtual world. For guidance, see [Playing audio](../patterns/playing-audio) and [Playing haptics](../patterns/playing-haptics).
> 오디오와 햅틱을 사용하여 몰입감을 향상시킵니다. 음향 효과 또는 범프 감지는 가상 물체가 물리적 표면 또는 다른 가상 물체와 접촉했음을 확인하는 좋은 방법입니다. 배경 음악은 또한 가상 세계에서 사람들을 감싸는데 도움을 줄 수 있다. 자세한 내용은 오디오 재생 및 햅틱 재생을 참조하십시오.
>




**Minimize text in the environment.** Display only the information that people need for your app experience.
> 환경에서 텍스트를 최소화합니다. 앱 경험에 필요한 정보만 표시합니다.
>




**If additional information or controls are necessary, consider displaying them in screen space.** Content in *screen space* appears fixed to a consistent location either in the virtual world or, less commonly, on the device screen. It’s typically easy for people to find and view content in screen space because it remains stationary while the underlying AR environment moves with the device.
> 추가 정보나 컨트롤이 필요한 경우 화면 공간에 표시하는 것을 고려하십시오. 화면 공간의 콘텐츠는 가상 세계에서 또는 드물게 장치 화면에서 일관된 위치에 고정된 것으로 나타납니다. 기본 AR 환경이 장치와 함께 이동하는 동안 화면 공간이 정지되어 있기 때문에 일반적으로 사람들이 화면 공간에서 콘텐츠를 찾고 보기 쉽습니다.
>




**Consider using indirect controls when you need to provide persistent controls.** *Indirect controls* are not part of the virtual environment — instead, they are 2D controls displayed in screen space. If people need access to persistent controls in your app, consider placing the controls so that people don’t have to adjust how they're holding the device to reach them. Also, consider using translucency in an indirect control to help avoid blocking the underlying scene. For example, the Measure app uses screen space to display a mix of translucent and opaque controls that people use to measure objects in the real world.
> 간접 컨트롤은 가상 환경의 일부가 아니라 화면 공간에 표시되는 2D 컨트롤입니다. 사용자가 앱에서 영구 컨트롤에 액세스해야 하는 경우 사용자가 해당 컨트롤에 도달하기 위해 장치를 잡는 방법을 조정할 필요가 없도록 컨트롤을 배치하는 것을 고려하십시오. 또한 기본 장면을 차단하지 않도록 간접 제어에서 투명성을 사용하는 것을 고려하십시오. 예를 들어 Measure 앱은 화면 공간을 사용하여 사람들이 실제 세계에서 물체를 측정하는 데 사용하는 반투명 및 불투명 컨트롤의 혼합을 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/arkit-measure-lines_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/arkit-measure-lines_2x.png)

**Anticipate that people will use your app in a wide variety of real-world environments.** People may open your app in a place where there isn't much room to move around or there aren't any large, flat surfaces. Clearly communicate your app's requirements and expectations to people up front to help them understand how their physical environment can affect their AR experience. You might also consider offering different sets of features for use in different environments.
> 사람들이 이동할 공간이 많지 않거나 크고 평평한 곳에서 앱을 열 수 있습니다. 애플리케이션의 요구 사항과 기대 사항을 사전에 명확하게 전달하여 물리적 환경이 AR 경험에 어떤 영향을 미칠 수 있는지 이해할 수 있도록 지원합니다. 또한 다른 환경에서 사용할 수 있도록 다른 기능 집합을 제공하는 것을 고려할 수도 있습니다.
>




**Be mindful of people's comfort.** Holding a device at a certain distance or angle for a prolonged period can be fatiguing. To help avoid causing fatigue, consider placing objects at a distance that reduces the need to move the device closer to the object; in a game, consider keeping levels short and intermixed with brief periods of downtime.
> 사람들의 편안함을 염두에 두십시오. 기기를 일정한 거리나 각도로 장시간 고정하는 것은 피곤할 수 있습니다. 피로를 유발하지 않도록 하려면 장치를 물체에 더 가까이 이동할 필요를 줄일 수 있는 거리에 물체를 배치하는 것을 고려해야 한다. 게임에서 레벨을 짧게 유지하고 짧은 다운타임과 혼합하는 것을 고려해야 한다.
>




**If your app encourages people to move, introduce motion gradually.** For example, you might not want to make people dodge a virtual projectile as soon as they enter your AR game. Give people time to adapt to the AR experience in your app and then progressively encourage movement.
> 예를 들어, 당신은 AR 게임에 들어가자마자 가상 발사체를 피하게 하는 것을 원치 않을 수도 있다. 사람들에게 당신의 앱에서 AR 경험에 적응할 시간을 준 다음 점진적으로 움직임을 장려하세요.
>




**Be mindful of people's safety.** When people are immersed in an AR experience, they're not necessarily aware of their physical surroundings, so making rapid, sweeping, or expansive motions might be dangerous. Consider ways of making your app safe to operate; for example, a game could avoid encouraging large or sudden movements.
> 사람들의 안전에 주의하라. 사람들이 AR 경험에 몰입할 때, 그들은 반드시 그들의 물리적 환경을 인식하지 못하기 때문에, 빠르고, 쓸어내리거나, 팽창하는 동작을 하는 것은 위험할 수 있다. 예를 들어, 게임이 크거나 갑작스러운 움직임을 유발하지 않도록 앱을 안전하게 작동하는 방법을 고려해 보십시오.
>




# **Using coaching to get people started**
> 코칭을 사용하여 사람들을 시작
>




Before people can enjoy an AR experience in your app, they need to move their device in ways that lets ARKit evaluate the surroundings and detect surfaces. In iOS 13 and later, you can use the built-in coaching view to show people what to do and provide feedback during the initialization process. You can also use the coaching view to help people reinitialize AR — a process known as *relocalization* — after an AR experience is interrupted by, for example, people switching briefly to a different app. For guidance on relocalization, see [Handling interruptions](https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality#handling-interruptions); for developer guidance, see [ARCoachingOverlayView](https://developer.apple.com/documentation/arkit/arcoachingoverlayview).
> 사람들이 당신의 앱에서 AR 경험을 즐기기 전에, 그들은 ARKit가 주변을 평가하고 표면을 감지할 수 있는 방식으로 기기를 움직여야 한다. iOS 13 이상에서는 기본 제공 코칭 뷰를 사용하여 초기화 프로세스 중에 사용자에게 수행할 작업을 보여주고 피드백을 제공할 수 있습니다. 또한 코칭 뷰를 사용하여 다른 앱으로 잠시 전환하는 등의 이유로 AR 경험이 중단된 후 AR을 재초기화할 수 있습니다. 위치 조정에 대한 지침은 중단 처리를 참조하고, 개발자 지침은 A 코치 오버레이 보기를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/arkit-horizontal-orientation_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/arkit-horizontal-orientation_2x.png)

**Hide unnecessary app UI while people are using a coaching view.** By default, the coaching view appears automatically when initialization or relocalization starts, so you should be prepared to hide unrelated UI to help people focus on the coaching view’s instructions.
> 사용자가 코칭 보기를 사용하는 동안 불필요한 앱 UI를 숨깁니다. 기본적으로 초기화 또는 재배치가 시작될 때 코칭 보기가 자동으로 표시되므로, 코칭 보기의 지침에 집중할 수 있도록 관련 없는 UI를 숨길 준비가 되어 있어야 합니다.
>




**If necessary, offer a custom coaching experience.** Although you can configure the system-provided coaching view to help people provide specific information — such as the detection of a horizontal or vertical plane — you might need additional information or want to use a different visual style. If you want to design a custom coaching experience, use the system-provided coaching view for reference.
> 필요한 경우 맞춤형 코칭 환경을 제공합니다. 수평면 또는 수직면 감지와 같은 특정 정보를 제공하도록 시스템에서 제공하는 코칭 보기를 구성할 수 있지만 추가 정보가 필요하거나 다른 시각적 스타일을 사용하고 싶을 수 있습니다. 맞춤형 코칭 환경을 설계하려면 시스템에서 제공하는 코칭 보기를 참조하십시오.
>




# **Helping people place objects**

**Show people when to locate a surface and place an object.** You can use the system-provided coaching view to help people find a horizontal or vertical flat surface on which to place an object. After ARKit detects a surface, your app can display a custom visual indicator to show when object placement is possible. You can help people understand how the placed object will look in the environment by aligning your indicator with the plane of the detected surface.
> 사용자에게 지표면을 찾고 객체를 배치할 시기를 보여줍니다. 시스템에서 제공하는 코칭 보기를 사용하여 사용자가 객체를 배치할 수평 또는 수직 평면을 찾는 데 도움을 줄 수 있습니다. ARKit가 표면을 감지한 후, 앱은 객체 배치가 가능한 시기를 보여주는 사용자 지정 시각적 표시기를 표시할 수 있습니다. 표시기를 탐지된 지표면의 평면에 맞춰 배치된 객체가 환경에서 어떻게 표시되는지 사람들이 이해할 수 있도록 도와줄 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/ARKit_Target_3.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/ARKit_Target_3.svg)

App-specific indicator

**When people place an object, immediately integrate that object into the AR environment.**Although surface detection quickly and progressively refines accuracy, it's best to avoid waiting for more accurate data before placing an object. Use the information available to respond instantly when people place an object; then, when surface detection completes, subtly refine the object's position if necessary. For example, if people place an object beyond the bounds of the detected surface, gently nudge the object back onto the surface. For developer guidance on refining an object's position, see [ARTrackedRaycast](https://developer.apple.com/documentation/arkit/artrackedraycast).
> 사람들이 객체를 배치할 때, 즉시 그 객체를 AR 환경에 통합하십시오.표면 감지는 빠르고 점진적으로 정확도를 개선하지만, 물체를 배치하기 전에 더 정확한 데이터를 기다리는 것은 피하는 것이 가장 좋습니다. 사용 가능한 정보를 사용하여 사용자가 객체를 배치할 때 즉시 응답한 다음 표면 탐지가 완료되면 필요한 경우 객체의 위치를 미세 조정합니다. 예를 들어, 사람들이 탐지된 지표면의 경계를 벗어난 곳에 객체를 배치하는 경우 객체를 지표면으로 다시 부드럽게 밀어넣습니다. 개체의 위치를 세분화하는 개발자 지침은 ARTrackedRaycast를 참조하십시오.
>




**Consider guiding people toward offscreen virtual objects.** Sometimes, it can be difficult for people to locate an object that’s positioned offscreen. When this is the case, you can help people find such objects by offering visual or audible cues. For example, if an object is offscreen to the left, you could display an indicator along the left edge of the screen that guides people to point the camera in that direction.
> 화면 밖의 가상 개체로 사람들을 안내하는 것을 고려해 보십시오. 화면 밖에 있는 개체를 찾는 것이 어려울 수 있습니다. 이 경우 시각적 또는 청각적 신호를 제공하여 사람들이 이러한 물체를 찾는 데 도움을 줄 수 있습니다. 예를 들어, 개체가 화면 왼쪽에 없는 경우 화면의 왼쪽 가장자리를 따라 표시기를 표시하여 사용자가 해당 방향으로 카메라를 가리키도록 할 수 있습니다.
>




**Avoid trying to precisely align objects with the edges of detected surfaces.** In AR, surface boundaries are approximations that may change as people's surroundings are further analyzed.
> 감지된 표면의 가장자리에 물체를 정확하게 맞추려고 시도하는 것을 피하십시오. AR에서 표면 경계는 사람들의 주변 환경이 추가로 분석됨에 따라 변경될 수 있는 근사치입니다.
>




**Incorporate plane classification information to inform object placement.** For example, only let people place a virtual piece of furniture on a plane that's classified as “floor,” or require a plane to be classified as “table” in order to place a virtual game board.
> 평면 분류 정보를 통합하여 객체 배치를 알려줍니다. 예를 들어, 사람들이 "바닥"으로 분류된 평면에 가상 가구를 배치하도록 하거나, 가상 게임 보드를 배치하기 위해 평면을 "테이블"로 분류하도록 요구합니다.
>




# **Designing intuitive, delightful object interactions**
> 직관적이고 즐거운 객체 상호 작용 설계
>




**Let people use direct manipulation to interact with objects when possible.** It’s more immersive and intuitive when people can interact with onscreen 3D objects by touching them directly, than by using indirect controls in screen space. However, in situations where people are moving around as they use your app, indirect controls can work better.
> 화면 공간에서 간접적인 컨트롤을 사용하는 것보다 화면상의 3D 객체를 직접 터치함으로써 사람들이 직접 조작할 수 있도록 하는 것이 더 몰입적이고 직관적이다. 그러나 사용자가 앱을 사용하면서 이동하는 상황에서는 간접 제어가 더 잘 작동할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/ARKit_User_Interaction_Right.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/ARKit_User_Interaction_Right.svg)

Direct manipulation

![https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/ARKit_User_Interaction_Wrong.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/ARKit_User_Interaction_Wrong.svg)

Indirect controls

**Let people directly interact with virtual objects using standard, familiar gestures.** For example, consider supporting a single-finger drag gesture for moving objects, and a two-finger rotation gesture for spinning objects. For guidance, see [Touchscreen gestures](../inputs/touchscreen-gestures).
> 사람들이 익숙한 표준 제스처를 사용하여 가상 개체와 직접 상호 작용할 수 있도록 합니다. 예를 들어 움직이는 개체에는 손가락 하나로 끌기 제스처를 지원하고 회전하는 개체에는 손가락 두 개로 회전 제스처를 지원하는 것을 고려해 보십시오. 자세한 내용은 터치 스크린 제스처를 참조하십시오.
>




**In general, keep interactions simple.** Touch gestures are inherently two-dimensional, but an AR experience involves the three dimensions of the real world. Consider the following approaches to simplifying user interactions with virtual objects.
> 일반적으로 상호작용을 단순하게 유지해야 한다. 터치 제스처는 본질적으로 2차원이지만 AR 경험은 실제 세계의 3차원을 포함한다. 가상 개체와의 사용자 상호 작용을 단순화하기 위한 다음과 같은 접근 방식을 고려해 보십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/ARKit_10.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/ARKit_10.svg)

Limit movement to the two-dimensional surface on which the object rests.
> 물체가 놓여 있는 2차원 표면으로 이동을 제한합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/ARKit_09.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/ARKit_09.svg)

Limit object rotation to a single axis.
> 개체 회전을 단일 축으로 제한합니다.
>




**Respond to gestures within reasonable proximity of interactive virtual objects.** It can be difficult for people to be precise when aiming to touch specific points on objects that are small, thin, or placed at a distance. When your app detects a gesture near an interactive object, it's usually best to assume that people want to affect that object.
> 상호작용하는 가상 물체의 합리적인 거리 내에서 제스처에 반응한다. 사람들이 작거나 얇거나 먼 곳에 있는 물체의 특정 지점을 만지는 것을 목표로 할 때 정확하기 어려울 수 있다. 당신의 앱이 대화형 객체 근처에서 제스처를 감지할 때, 일반적으로 사람들이 그 객체에 영향을 주고 싶어한다고 가정하는 것이 가장 좋다.
>




**Support user-initiated object scaling when it makes sense in your app.** For example, if your app lets people explore an imaginary environment, it probably makes sense to support object scaling because your app doesn’t need to represent the real world. On the other hand, if your app helps shoppers decide on furniture to buy, letting people scale a chair object doesn’t help them visualize how the chair will look in a room.
> 앱에서 사용자가 시작한 개체 크기 조정을 지원합니다. 예를 들어, 앱이 사람들이 가상 환경을 탐색하도록 허용하는 경우, 앱이 실제 세계를 나타낼 필요가 없기 때문에 개체 크기 조정을 지원하는 것이 합리적일 수 있습니다. 반면에, 당신의 앱이 쇼핑객들이 구매할 가구를 결정하는 데 도움이 된다면, 사람들이 의자 물체의 크기를 조정하도록 하는 것은 그들이 방에서 의자가 어떻게 보일지 상상하는 데 도움이 되지 않는다.
>




**TIP**Regardless of the purpose of your app, don’t use scaling as a way to adjust the distance of an object. If you enlarge a distant object in an effort to make it appear closer, the result is a larger object that still looks far away.
> 팁앱의 목적과 상관없이, 물체의 거리를 조정하는 방법으로 스케일링을 사용하지 마십시오. 멀리 있는 물체를 더 가까이 보이게 하기 위해 확대하면, 그 결과는 여전히 멀리 보이는 더 큰 물체가 된다.
>




**Be wary of potentially conflicting gestures.** A two-finger pinch gesture, for example, is similar to a two-finger rotation gesture. If you implement two similar gestures like this, be sure to test your app and make sure they're interpreted properly.
> 충돌 가능성이 있는 제스처를 주의하십시오. 예를 들어, 두 손가락으로 꼬집는 제스처는 두 손가락으로 회전하는 제스처와 유사합니다. 이와 같은 두 가지 유사한 제스처를 구현하는 경우 앱을 테스트하고 제대로 해석되는지 확인하십시오.
>




**Strive for virtual object movement that’s consistent with the physics of your app’s AR environment.** People don’t necessarily expect an object to move smoothly over a rough or uneven surface, but they do expect objects to remain visible during movement. Aim to keep moving objects attached to real-world surfaces and avoid causing objects to jump or vanish and reappear as people resize, rotate, or move them.
> 앱의 AR 환경 물리학과 일치하는 가상 객체 이동을 위해 노력하십시오. 사람들은 객체가 거칠거나 울퉁불퉁한 표면 위에서 부드럽게 이동하기를 반드시 기대하지는 않지만 이동 중에도 객체가 계속 눈에 띄기를 기대합니다. 움직이는 물체를 실제 표면에 부착한 상태로 유지하고 사람들이 물체의 크기를 조정하거나 회전하거나 움직일 때 물체가 점프하거나 사라지거나 다시 나타나지 않도록 합니다.
>




**Explore even more engaging methods of interaction.** Gestures aren't the only way for people to interact with virtual objects in AR. Your app can use other factors, like motion and proximity, to bring content to life. A game character, for example, could turn its head to look at a person as they walk toward it.
> 훨씬 더 매력적인 상호 작용 방법을 탐구하십시오. 제스처는 사람들이 AR에서 가상 물체와 상호 작용하는 유일한 방법이 아닙니다. 당신의 앱은 움직임과 근접성과 같은 다른 요소들을 사용하여 콘텐츠에 생명을 불어넣을 수 있다. 예를 들어, 게임 캐릭터는 그들이 그 쪽으로 걸어갈 때 사람을 보기 위해 고개를 돌릴 수 있다.
>




# **Designing a great multiuser experience**
> 우수한 다중 사용자 환경 설계
>




When multiple people share your app's AR experience, each participant maps the environment independently and ARKit automatically merges the maps. For developer guidance, see [isCollaborationEnabled](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/3152987-iscollaborationenabled).
> 여러 명이 앱의 AR 경험을 공유하면 각 참가자는 환경을 독립적으로 매핑하고 ARKit는 자동으로 맵을 병합합니다. 개발자 지침은 isCollaborationEnabled를 참조하십시오.
>




**Consider enabling people occlusion.** If your app supports placing virtual objects behind people who appear in the device’s camera feed, enhance the illusion of reality by letting the people occlude the objects. For developer guidance, see [Occluding virtual content with people](https://developer.apple.com/documentation/arkit/occluding_virtual_content_with_people).
> 사용자 폐색을 활성화하는 것을 고려해 보십시오. 만약 당신의 앱이 장치의 카메라 피드에 나타나는 사용자 뒤에 가상 물체를 배치하는 것을 지원한다면, 사용자가 물체를 폐색하도록 함으로써 현실에 대한 환상을 강화하십시오. 개발자 지침은 사용자와 함께 가상 콘텐츠 차단을 참조하십시오.
>




**When possible, let new participants enter a multiuser AR experience.** Unless your app requires all participants to join before the experience begins, consider using implicit map merging to let new people quickly join an ongoing AR experience. For developer guidance, see [isCollaborationEnabled](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/3152987-iscollaborationenabled).
> 가능한 경우, 새로운 참가자가 다중 사용자 AR 경험을 입력하도록 합니다. 당신의 앱이 모든 참가자가 경험을 시작하기 전에 참여하도록 요구하지 않는 한, 새로운 사람들이 진행 중인 AR 경험에 빠르게 참여할 수 있도록 암시적 맵 병합을 사용하는 것을 고려하십시오. 개발자 지침은 isCollaborationEnabled를 참조하십시오.
>




# **Reacting to real-world objects**

You can enhance an AR experience by using known images and objects in the real-world environment to trigger the appearance of virtual content. For example, an app that recognizes theater posters for a sci-fi film could cause virtual space ships to emerge from the posters and fly around the environment. Another example is an app for an art museum that presents a virtual tour guide when it recognizes a sculpture. To enable experiences like these, your app provides a set of 2D reference images or 3D reference objects, and ARKit indicates when and where it detects any of these items in the current environment. For developer guidance, see [Recognizing images in an AR experience](https://developer.apple.com/documentation/arkit/recognizing_images_in_an_ar_experience).
> 실제 환경에서 알려진 이미지와 개체를 사용하여 가상 콘텐츠의 모양을 트리거하여 AR 경험을 향상시킬 수 있습니다. 예를 들어, 공상과학 영화를 위해 극장 포스터를 인식하는 앱은 포스터에서 가상 우주선이 나타나 환경을 날아다니게 할 수 있다. 조각을 인식하면 가상 투어 가이드를 제공하는 미술관용 앱도 있다. 이러한 경험을 가능하게 하기 위해 앱은 2D 참조 이미지 또는 3D 참조 개체 세트를 제공하고 ARKit는 현재 환경에서 이러한 항목을 탐지하는 시기와 위치를 나타냅니다. 개발자 지침은 AR 환경에서 이미지 인식을 참조하십시오.
>




**When a detected image first disappears, consider delaying the removal of virtual objects that are attached to it.** ARKit doesn’t track changes to the position or orientation of each detected image. To help prevent virtual objects from flickering, consider waiting up to one second before fading them out or removing them.
> 탐지된 이미지가 처음 사라지면 이미지에 연결된 가상 개체의 제거를 지연시키는 것이 좋습니다. ARKit는 탐지된 각 이미지의 위치 또는 방향 변경을 추적하지 않습니다. 가상 개체가 깜박이는 것을 방지하려면 가상 개체를 페이드 아웃하거나 제거하기 전에 최대 1초까지 기다리는 것이 좋습니다.
>




**Limit the number of reference images in use at one time.** Image detection performance works best when ARKit looks for 100 or fewer distinct images in the real-world environment. If you need more than 100 reference images, you can change the set of active reference images based on context. For example, a museum guide app could ask permission to use location services to determine the part of the museum a person is in, and then look only for images displayed in that area.
> 한 번에 사용되는 참조 이미지 수를 제한합니다. 이미지 감지 성능은 ARKit가 실제 환경에서 100개 이하의 고유한 이미지를 찾을 때 가장 잘 작동합니다. 기준 영상이 100개 이상 필요한 경우 컨텍스트를 기준으로 활성 기준 영상 세트를 변경할 수 있습니다. 예를 들어, 박물관 안내 앱은 사람이 있는 박물관의 부분을 결정하기 위해 위치 서비스 사용 허가를 요청한 다음 그 지역에 표시된 이미지만 찾을 수 있다.
>




**Limit the number of reference images requiring an accurate position.** Updating the position of a reference image requires more resources. Use a tracked image when the image may move in the environment or when an attached animation or virtual object is small compared to the size of the image.
> 정확한 위치가 필요한 참조 이미지 수를 제한합니다. 참조 이미지의 위치를 업데이트하려면 더 많은 리소스가 필요합니다. 이미지가 환경에서 이동할 수 있거나 첨부된 애니메이션 또는 가상 개체가 이미지 크기에 비해 작을 때 추적된 이미지를 사용합니다.
>




# **Communicating with people**

**If you must display instructional text, use approachable terminology.** AR is an advanced concept that may be intimidating to some people. To help make it approachable, avoid using technical terms like ARKit, world detection, and tracking. Instead, use friendly, conversational terms that most people will understand.
> 만약 당신이 지시문을 표시해야 한다면, 접근 가능한 용어를 사용하세요. AR은 어떤 사람들에게는 위협적일 수 있는 진보된 개념입니다. 접근 가능하도록 하려면 ARKit, 세계 탐지 및 추적과 같은 기술 용어를 사용하지 마십시오. 대신, 대부분의 사람들이 이해할 수 있는 친근하고 대화가 가능한 용어를 사용하세요.
>




| Do | Don't |
| --- | --- |
| Unable to find a surface. Try moving to the side or repositioning your phone. | Unable to find a plane. Adjust tracking. |
| Tap a location to place the [name of object to be placed]. | Tap a plane to anchor an object. |
| Try turning on more lights and moving around. | Insufficient features. |
| Try moving your phone more slowly. | Excessive motion detected. |

**In a three-dimensional context, prefer 3D hints.** For example, placing a 3D rotation indicator around an object is more intuitive than displaying text-based instructions in a 2D overlay. Avoid displaying textual overlay hints in a 3D context unless people aren’t responding to contextual hints.
> 3차원 환경에서는 3D 힌트를 선호합니다. 예를 들어, 물체 주위에 3D 회전 표시기를 배치하는 것이 2D 오버레이에 텍스트 기반 명령을 표시하는 것보다 더 직관적입니다. 사람들이 상황에 맞는 힌트에 응답하지 않는 한 3D 컨텍스트에 텍스트 오버레이 힌트를 표시하지 마십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/ARKit_11.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/ARKit_11.svg)

Prefer a 3D hint in a 3D context.
> 3D 컨텍스트에서 3D 힌트를 선호합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/ARKit_06.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/ARKit_06.svg)

If necessary, use a 2D hint in a 3D context.
> 필요한 경우 3D 컨텍스트에서 2D 힌트를 사용합니다.
>




**Make important text readable.** Use screen space to display text used for critical labels, annotations, and instructions. If you need to display text in 3D space, make sure the text faces people and that you use the same type size regardless of the distance between the text and the labeled object.
> 중요한 텍스트를 읽을 수 있도록 합니다. 화면 공간을 사용하여 중요한 레이블, 주석 및 지침에 사용되는 텍스트를 표시합니다. 3D 공간에 텍스트를 표시해야 하는 경우 텍스트가 사람을 향하고 텍스트와 레이블이 지정된 개체 사이의 거리에 관계없이 동일한 유형 크기를 사용해야 합니다.
>




**If necessary, provide a way to get more information.** Design a visual indicator that fits with your app experience to show people that they can tap for more information.
> 필요한 경우 더 많은 정보를 얻을 수 있는 방법을 제공하십시오. 앱 경험에 맞는 시각적 표시기를 설계하여 사용자가 더 많은 정보를 얻을 수 있음을 보여줍니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/arkit-labels_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/arkit-labels_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/arkit-popover_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/arkit-popover_2x.png)

# **Handling interruptions**

ARKit can't track device position and orientation during an interruption, such as when people briefly switch to another app or accept a phone call. After an interruption ends, previously placed virtual objects are likely to appear in the wrong real-world positions. When you enable relocalization, ARKit attempts to restore those virtual objects to their original real-world positions using new information. For developer guidance, see [Managing session lifecycle and tracking quality](https://developer.apple.com/documentation/arkit/managing_session_lifecycle_and_tracking_quality).
> ARKit는 사람들이 다른 앱으로 잠시 전환하거나 전화를 받을 때와 같이 중단되는 동안 장치 위치와 방향을 추적할 수 없습니다. 중단이 끝나면 이전에 배치된 가상 객체가 잘못된 실제 위치에 나타날 수 있습니다. 재배치를 사용하도록 설정하면 ARKit는 새 정보를 사용하여 이러한 가상 개체를 원래 실제 위치로 복원하려고 시도합니다. 개발자 지침은 세션 수명 주기 관리 및 품질 추적을 참조하십시오.
>




**Consider using the system-provided coaching view to help people relocalize.** During relocalization, ARKit attempts to reconcile its previous state with new observations of the current environment. To enable these observations, you can use the coaching view to help people return the device to its previous position and orientation.
> 시스템이 제공하는 코칭 뷰를 사용하여 사람들이 재로컬리제이션하는 동안 ARKit는 이전 상태를 현재 환경에 대한 새로운 관찰과 조정하려고 시도한다. 이러한 관찰을 활성화하기 위해 코칭 보기를 사용하여 사용자가 장치를 이전 위치와 방향으로 되돌릴 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/arkit-vertical-orientation_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/augmented-reality/images/arkit-vertical-orientation_2x.png)

