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

