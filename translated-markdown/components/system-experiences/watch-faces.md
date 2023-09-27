# **[components-status] watch-faces**

## A watch face is a view that people choose as their primary view in watchOS.
> 워치페이스는 사람들이 시계에서 그들의 주요 보기로 선택하는 뷰이다.운영 체제
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/faces-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/faces-intro-dark_2x.png)

The watch face is at the heart of the watchOS experience. People choose a watch face they want to see every time they raise their wrist, and they customize it with their favorite complications. People can even customize different watch faces for different activities, so they can switch to the watch face that fits their current context.
> 시계의 얼굴은 시계의 중심에 있다.OS 경험. 사람들은 손목을 들 때마다 보고 싶은 시계 얼굴을 선택하고, 자신이 좋아하는 합병증에 맞춰 맞춤 제작한다. 사람들은 심지어 다른 활동을 위해 다른 시계 얼굴을 사용자 정의할 수 있어서, 그들은 그들의 현재 상황에 맞는 시계 얼굴로 전환할 수 있다.
>




In watchOS 7 and later, people can share the watch faces they configure. For example, a fitness instructor might configure a watch face to share with their students by choosing the Gradient watch face, customizing the color, and adding their favorite health and fitness complications. When the students add the shared watch face to their Apple Watch or the Watch app on their iPhone, they get a custom experience without having to configure it themselves.
> 당직중OS 7 이상에서는 사람들이 구성한 시계 얼굴을 공유할 수 있다. 예를 들어, 피트니스 강사는 그라데이션 워치 페이스를 선택하고 색상을 사용자 지정하고 좋아하는 건강 및 피트니스 합병증을 추가하여 학생들과 공유할 워치 페이스를 구성할 수 있습니다. 학생들이 공유된 워치 페이스를 애플 워치나 아이폰의 워치 앱에 추가하면, 그들은 그것을 직접 구성할 필요 없이 맞춤형 경험을 얻을 수 있다.
>




You can also configure a watch face to share from within your app, on your website, or through Messages, Mail, or social media. Offering shareable watch faces can help you introduce more people to your complications and your app.
> 또한 앱 내, 웹 사이트 또는 메시지, 메일 또는 소셜 미디어를 통해 공유할 워치페이스를 구성할 수 있습니다. 공유 가능한 시계 얼굴을 제공하면 더 많은 사람들에게 당신의 복잡성과 앱을 소개하는 데 도움이 될 수 있다.
>




# **Best practices**

**Help people discover your app by sharing watch faces that feature your complications.** Ideally, you support multiple complications so that you can showcase them in a shareable watch face and provide a curated experience. For some watch faces, you can also specify a system accent color, images, or styles. If people add your watch face but haven't installed your app, the system prompts them to install it.
> 당신의 복잡성을 특징으로 하는 시계 얼굴을 공유함으로써 사람들이 당신의 앱을 찾을 수 있도록 도와주세요. 이상적으로는 당신은 공유 가능한 시계 얼굴로 그것들을 보여주고 큐레이티드 경험을 제공할 수 있도록 여러 가지 복잡한 것들을 지원합니다. 일부 시계 면의 경우 시스템 액센트 색상, 이미지 또는 스타일을 지정할 수도 있습니다. 다른 사용자가 시계 페이스를 추가했지만 앱을 설치하지 않은 경우 시스템에서 설치하라는 메시지를 표시합니다.
>




**Display a preview of each watch face you share.** Displaying a preview that highlights the advantages of your watch face can help people visualize its benefits. You can get a preview by using the iOS Watch app to email the watch face to yourself. The preview includes an illustrated device bezel that frames the face and is suitable for display on websites and in watchOS and iOS apps. Alternatively, you can replace the illustrated bezel with a high-fidelity hardware bezel that you can download from [Apple Design Resources](https://developer.apple.com/design/resources/#product-bezels)and composite onto the preview. For developer guidance, see [Sharing an Apple Watch face](https://developer.apple.com/documentation/clockkit/sharing_an_apple_watch_face).
> 공유하는 각 시계 면의 미리 보기를 표시합니다. 시계 면의 장점을 강조하는 미리 보기를 표시하면 사람들이 시계 면의 이점을 시각화하는 데 도움이 될 수 있습니다. iOS Watch 앱을 사용하여 미리 보기를 통해 워치 페이스를 자신에게 이메일로 보낼 수 있습니다. 프리뷰에는 얼굴을 액자에 넣은 일러스트 장치 베젤이 포함되어 있으며, 웹사이트와 워치OS, iOS 앱에 표시하기에 적합하다. 또는 그림에 표시된 베젤을 Apple Design Resources에서 다운로드하여 미리 보기에 합성할 수 있는 충실도가 높은 하드웨어 베젤로 교체할 수 있습니다. 개발자 지침은 Apple Watch 페이스 공유를 참조하십시오.
>




**Aim to offer shareable watch faces for all Apple Watch devices.** Some watch faces are available on Series 4 and later — such as California, Chronograph Pro, Gradient, Infograph, Infograph Modular, Meridian, Modular Compact, and Solar Dial — and Explorer is available on Series 3 (with cellular) and later. If you use one of these faces in your configuration, you should offer a similar configuration using a face that's available on Series 3 and earlier. To help people make a choice, you can clearly label each shareable watch face with the devices it supports.
> 캘리포니아, 크로노그래프 프로, 그라데이션, 인포그래프, 인포그래프 모듈러, Meridian, Modular Compact 및 Solar Dial과 같은 일부 워치 페이스는 시리즈 4 이상에서 사용할 수 있으며 탐색기는 시리즈 3 이상(셀룰러 포함)에서 사용할 수 있습니다. 구성에서 이러한 면 중 하나를 사용하는 경우 Series 3 이전 버전에서 사용할 수 있는 면을 사용하여 유사한 구성을 제공해야 합니다. 사용자가 선택할 수 있도록 각 공유 가능한 워치페이스에 지원하는 장치를 명확하게 레이블링할 수 있습니다.
>




**Respond gracefully if people choose an incompatible watch face.** The system sends your app an error when people try to use an incompatible watch face on Series 3 or earlier. In this scenario, consider immediately offering an alternative configuration that uses a compatible face instead of displaying an error. Along with the previews you provide, help people understand that they might receive an alternative watch face if they choose a face that isn't compatible with their Apple Watch.
> 사용자가 호환되지 않는 워치페이스를 선택한 경우 우아하게 응답하십시오. 시리즈 3 이전 버전에서 사용자가 호환되지 않는 워치페이스를 사용하려고 하면 시스템이 앱에 오류를 보냅니다. 이 시나리오에서는 오류를 표시하는 대신 호환되는 면을 사용하는 대체 구성을 즉시 제공하는 것을 고려하십시오. 제공하는 미리 보기와 함께 사용자가 Apple Watch와 호환되지 않는 얼굴을 선택할 경우 다른 시계 얼굴을 받을 수 있음을 이해할 수 있습니다.
>




# **Platform considerations**

*Not supported in iOS, iPadOS, macOS, or tvOS.*
> iOS, iPadOS, macOS 또는 tvOS에서는 지원되지 않습니다.
>



