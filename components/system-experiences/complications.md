# **[components-status] complications**
## A complication displays timely, relevant information on the watch face, where people can view it each time they raise their wrist.
> 합병증은 손목을 들 때마다 사람들이 볼 수 있는 시계 표면에 적시에 관련 정보를 표시한다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/complications-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/complications-intro-dark_2x.png)

People often prefer apps that provide multiple, powerful complications, because it gives them quick ways to view the data they care about, even when they don’t open the app.
> 사람들은 종종 여러 가지 강력한 복잡성을 제공하는 앱을 선호하는데, 이는 앱을 열지 않을 때에도 관심 있는 데이터를 빠르게 볼 수 있는 방법을 제공하기 때문입니다.
>




Most watch faces can display at least one complication; some can display four or more.
> 대부분의 워치페이스는 적어도 하나의 합병증을 표시할 수 있으며, 일부는 4개 이상을 표시할 수 있다.
>




Starting in watchOS 9, the system organizes complications (also known as *accessories*) into several families — like [circular](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications#circular) and [inline](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications#inline) — and defines some recommended layouts you can use to display your complication data. A watch face can specify the family it supports in each complication slot. Complications that work in earlier versions of watchOS can use the [legacy templates](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications#legacy-templates), which define nongraphic complication styles that don’t take on a wearer’s selected color.
> 시계에서 시작하기OS 9에서 이 시스템은 복잡한(액세서리라고도 함)을 원형 및 인라인과 같은 여러 제품군으로 구성하고 복잡한 데이터를 표시하는 데 사용할 수 있는 몇 가지 권장 레이아웃을 정의합니다. 워치페이스는 각 합병증 슬롯에서 지원하는 패밀리를 지정할 수 있습니다. 이전 버전의 시계에서 작동하는 합병증OS는 기존 템플릿을 사용할 수 있으며, 이 템플릿은 착용자가 선택한 색상을 띠지 않는 비그래픽 복잡성 스타일을 정의합니다.
>




You provide the data for a complication in the form of a timeline that the system uses to determine the data to display at various times. You can update the timeline a limited number of times each day, and the system stores a limited number of timeline entries for each app. For developer guidance, see [Keeping your complications up to date](https://developer.apple.com/documentation/clockkit/keeping_your_complications_up_to_date).
> 시스템이 다양한 시간에 표시할 데이터를 결정하는 데 사용하는 타임라인 형태로 합병증에 대한 데이터를 제공합니다. 매일 제한된 횟수만큼 타임라인을 업데이트할 수 있으며 시스템은 각 앱에 대해 제한된 수의 타임라인 항목을 저장합니다. 개발자 지침은 복잡성을 최신 상태로 유지를 참조하십시오.
>




**DEVELOPER NOTE**Prefer using WidgetKit to develop complications for watchOS 9 and later. To support earlier versions of watchOS, continue to implement the ClockKit complication data source protocol (see [CLKComplicationDataSource](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/)). For additional guidance, see [Building complications with SwiftUI](https://developer.apple.com/documentation/clockkit/building_complications_with_swiftui).
> 개발자 메모는 WidgetKit를 사용하여 시계의 복잡성을 개발하는 것을 선호합니다.OS 9 이상. 이전 버전의 워치OS를 지원하려면 ClockKit 복잡한 데이터 소스 프로토콜을 계속 구현하십시오(CLKComplexion DataSource 참조). 자세한 내용은 Swift를 사용한 복잡성 구축을 참조하십시오.UI.
>




# **Best practices**

**Identify essential, dynamic content that people want to view at a glance.** Although people can use a complication to quickly launch an app, the complication behavior they appreciate more is the display of relevant information that always feels up to date. A static complication that doesn’t display meaningful data may be less likely to remain in a prominent position on the watch face.
> 사람들이 한 눈에 보고 싶어하는 필수적이고 역동적인 콘텐츠를 식별한다. 비록 사람들이 앱을 빠르게 실행하기 위해 복잡한 행동을 사용할 수 있지만, 그들이 더 높이 평가하는 것은 항상 최신으로 느껴지는 관련 정보의 표시이다. 의미 있는 데이터를 표시하지 않는 정적 합병증은 워치 페이스에서 눈에 띄는 위치에 남아 있을 가능성이 적을 수 있다.
>




**Support all complication families when possible.** Supporting more families means that your complications are available on more watch faces. If you can’t display useful information for a particular complication family, provide an image that represents your app — like your app icon — that still lets people launch your app from the watch face.
> 가능하면 모든 합병증 가족을 지원하십시오. 더 많은 가족을 지원한다는 것은 더 많은 감시자들이 당신의 합병증을 이용할 수 있다는 것을 의미합니다. 특정 합병증 패밀리에 대한 유용한 정보를 표시할 수 없는 경우 앱 아이콘과 같이 사용자의 앱을 나타내는 이미지를 제공하여 사용자가 워치페이스에서 앱을 시작할 수 있도록 합니다.
>




**Consider creating multiple complications for each family.** Supporting multiple complications helps you take advantage of shareable watch faces and lets people configure a watch face that’s focused on an app they love. For example, an app that helps people train for triathlons could offer three circular complications — one for each segment of the race — each of which deep-links to the segment-specific area in the app. This app could also offer a shareable watch face that’s preconfigured to include its swimming, biking, and running complications and to use its custom images and colors. When people choose this watch face, they don’t have to do any configuration before they can start using it. For guidance, see [Watch faces](../components/system-experiences/watch-faces); for developer guidance, see [Declaring complications for your app](https://developer.apple.com/documentation/clockkit/declaring_complications_for_your_app).
> 각 제품군에 대해 여러 가지 복잡성을 생성하는 것을 고려해 보십시오. 여러 복잡성을 지원하면 공유 가능한 워치페이스를 활용할 수 있고 사람들이 좋아하는 앱에 초점을 맞춘 워치페이스를 구성할 수 있습니다. 예를 들어, 트라이애슬론을 위해 훈련하는 사람들을 돕는 앱은 3개의 순환적인 합병증을 제공할 수 있다. 각각은 앱의 세그먼트별 영역으로 딥 링크된다. 이 앱은 또한 수영, 자전거, 달리기의 복잡성을 포함하고 사용자 지정 이미지와 색상을 사용하도록 미리 구성된 공유 가능한 워치 페이스를 제공할 수 있다. 사람들이 이 시계 면을 선택할 때, 그들은 그것을 사용하기 전에 어떤 구성도 할 필요가 없다. 자세한 내용은 얼굴 보기를 참조하십시오. 개발자 지침은 앱에 대한 합병증 선언을 참조하십시오.
>




**Define a different deep link for each complication you support.** It works well when each complication opens your app to the most relevant area. If all the complications you support open the same area in your app, they can seem less useful.
> 지원하는 각 합병증에 대해 서로 다른 심층 링크를 정의하십시오. 각 합병증이 가장 관련성이 높은 영역으로 앱을 열 때 잘 작동합니다. 만약 당신이 지원하는 모든 합병증들이 당신의 앱에서 같은 영역을 연다면, 그것들은 덜 유용해 보일 수 있다.
>




**Keep privacy in mind.** With the Always-On Retina display, information on the watch face might be visible to people other than the wearer. Make sure you help people prevent potentially sensitive information from being visible to others. For guidance, see [Always On](../technologies/always-on).
> Always-On Retina 디스플레이를 사용하면 착용자 이외의 사람이 시계 얼굴에 있는 정보를 볼 수 있습니다. 잠재적으로 중요한 정보가 다른 사람에게 표시되지 않도록 사용자를 도와주십시오. 자세한 내용은 항상 실행을 참조하십시오.
>




**Carefully consider when to update data.** Each timeline entry has a time value that specifies the time at which to display your data on the watch face; different data sets might require different time values. For example, a meeting app might display information about an upcoming meeting an hour before the meeting starts, but a weather app might display forecast information at the time those conditions are expected to occur. Choose times that enhance the usefulness of the data you supply.
> 데이터를 업데이트할 시기를 신중하게 고려하십시오. 각 타임라인 항목에는 워치페이스에 데이터를 표시할 시간을 지정하는 시간 값이 있습니다. 데이터 세트마다 다른 시간 값이 필요할 수 있습니다. 예를 들어, 미팅 앱은 미팅이 시작되기 한 시간 전에 예정된 미팅에 대한 정보를 표시할 수 있지만 날씨 앱은 이러한 조건이 발생할 것으로 예상되는 시간에 예측 정보를 표시할 수 있습니다. 제공하는 데이터의 유용성을 높이는 시간을 선택합니다.
>




# **Visual design**

**Choose a ring or gauge style based on the data you need to display.**Many families support a ring or gauge layout that provides consistent ways to represent numerical values that can change over time. For example:
> 표시해야 하는 데이터를 기준으로 링 또는 게이지 스타일을 선택합니다.많은 패밀리는 시간이 지남에 따라 변경될 수 있는 수치를 일관된 방법으로 표현할 수 있는 링 또는 게이지 레이아웃을 지원합니다. 예:
>




- The closed style can convey a value that’s a percentage of a whole, such as for a battery gauge.
- >  폐쇄형 스타일은 배터리 게이지와 같이 전체의 백분율에 해당하는 값을 전달할 수 있습니다.

- The open style works well when the minimum and maximum values are arbitrary — or don’t represent a percentage of the whole — like for a speed indicator.
- >  열린 스타일은 속도 표시기와 같이 최소값과 최대값이 임의이거나 전체의 백분율을 나타내지 않을 때 잘 작동합니다.

- Similar to the open style, the segmented style also displays values within an app-defined range, and can convey rapid value changes, such as in the Noise complication.
- >  열린 스타일과 마찬가지로 세그먼트 스타일도 앱 정의 범위 내의 값을 표시하며, 노이즈 합병증과 같은 빠른 값 변화를 전달할 수 있습니다.


**Make sure images look good in tinted mode.** In tinted mode, the system applies a solid color to a complication’s text, gauges, and images, and desaturates full-color images unless you provide tinted versions of them. (If you’re using legacy templates, tinted mode applies only to graphic complications.) To help your complications perform well in tinted mode:
> 색조 모드에서는 시스템이 복잡한 텍스트, 게이지 및 이미지에 단색을 적용하고 사용자가 색조 버전을 제공하지 않는 한 전체 색상 이미지를 불포화합니다.(기존 템플릿을 사용하는 경우에는 그래픽 복잡성에만 색조 모드가 적용됩니다.) 색조 모드에서 합병증이 잘 수행되도록 하려면 다음을 참조하십시오.
>




- Avoid using color as the only way to communicate important information. You want people to get the same information in tinted mode as they do in nontinted mode.
- >  중요한 정보를 전달하는 유일한 방법으로 색상을 사용하지 마십시오. 사람들이 색조 모드에서 색조 모드에서 얻는 것과 동일한 정보를 얻기를 참조하십시오.

- When necessary, provide an alternative tinted-mode version of a full-color image. If your full-color image doesn’t look good when it’s desaturated, you can supply a different version of the image for the system to use in tinted mode. For developer guidance, see [Display tinted complications](https://developer.apple.com/documentation/clockkit/graphic#3380124).
- >  필요한 경우 전체 색상 이미지의 대체 색조 모드 버전을 제공합니다. 전체 색상 이미지가 불포화 상태일 때 보기 좋지 않으면 시스템에서 색조 모드로 사용할 다른 버전의 이미지를 제공할 수 있습니다. 개발자 지침은 색조 복잡 표시를 참조하십시오.


**Recognize that people might prefer to use tinted mode for complications, instead of viewing them in full color.** When people choose tinted mode, the system automatically desaturates your complication, converting it to grayscale and tinting its images, gauges, and text using a single color that’s based on the wearer’s selected color.
> 사람들이 전체 색상으로 보는 대신 합병증에 대해 색조 모드를 사용하는 것을 선호할 수 있다는 것을 인식하십시오. 사람들이 색조 모드를 선택하면 시스템은 자동으로 합병증을 불포화시켜 그레이스케일로 변환하고 착용자가 선택한 색상에 기반한 단일 색상을 사용하여 이미지, 게이지 및 텍스트를 색조화합니다.
>




**When creating complication content, generally use line widths of two points or greater.** Thinner lines can be difficult to see at a glance, especially when the wearer is in motion. Use line weights that suit the size and complexity of the image.
> 합병증 콘텐츠를 만들 때는 일반적으로 2점 이상의 선폭을 사용한다. 특히 착용자가 움직일 때 선이 얇으면 한 눈에 보기 어려울 수 있다. 이미지의 크기와 복잡성에 적합한 선 두께를 사용합니다.
>




**Provide a set of static placeholder images for each complication you support.** The system uses placeholder images when there’s no other content to display for your complication’s data. For example, when people first install your app, the system can display a static placeholder while it checks to see if your app can generate a localized placeholder to use instead. Placeholder images can also appear in the carousel from which people select complications. Note that complication image sizes vary per layout (and per legacy template) and the size of a placeholder image may not match the size of the actual image you supply for that complication. For developer guidance, see [Adding placeholders for your complication](https://developer.apple.com/documentation/clockkit/adding_a_complication_to_your_watchos_app/adding_placeholders_for_your_complication).
> 지원하는 각 합병증에 대해 정적 자리 표시자 이미지 세트를 제공합니다. 합병증의 데이터에 대해 표시할 다른 콘텐츠가 없을 때 시스템은 자리 표시자 이미지를 사용합니다. 예를 들어, 사용자가 앱을 처음 설치할 때 시스템은 앱이 대신 사용할 현지화된 자리 표시자를 생성할 수 있는지 확인하는 동안 정적 자리 표시자를 표시할 수 있습니다. 자리 표시자 이미지는 사람들이 합병증을 선택하는 회전목마에도 나타날 수 있다. 복잡한 이미지 크기는 레이아웃(및 레거시 템플릿)마다 다르며 자리 표시자 이미지의 크기가 해당 복잡한 이미지에 대해 제공하는 실제 이미지의 크기와 일치하지 않을 수 있습니다. 개발자 지침은 복잡성에 대한 자리 표시자 추가를 참조하십시오.
>




# **Circular**

Circular layouts can include text, gauges, and full-color images in circular areas on the Infograph and Infograph Modular watch faces. The circular family also defines extra-large layouts for displaying content on the X-Large watch face.
> 원형 레이아웃에는 Infograph 및 Infograph Modular 시계 면의 원형 영역에 텍스트, 게이지 및 전체 색상 이미지가 포함될 수 있습니다. 원형 패밀리는 또한 X-Large 워치 페이스에 콘텐츠를 표시하기 위한 초대형 레이아웃을 정의합니다.
>




-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CircularClosedGaugeImage_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CircularClosedGaugeImage_2x.png)

Closed gauge image

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CircularClosedGaugeText_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CircularClosedGaugeText_2x.png)

Closed gauge text

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CircularOpenGaugeImage_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CircularOpenGaugeImage_2x.png)

Open gauge image

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CircularOpenGaugeSimpleText_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CircularOpenGaugeSimpleText_2x.png)

Open gauge text

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CircularOpenGaugeRangeText_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CircularOpenGaugeRangeText_2x.png)

Open gauge range

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/GraphicCircularImage_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/GraphicCircularImage_2x.png)

Image

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-circular-stack_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-circular-stack_2x.png)

Stack image

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-circular-stack-text_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-circular-stack-text_2x.png)

Stack text


You can also add text to accompany a regular-size circular image, using a design that curves the text along the bezel of some watch faces, like Infograph. The text can fill nearly 180 degrees of the bezel before truncating.
> Infograph와 같은 일부 시계 면의 베젤을 따라 텍스트를 곡선 처리하는 디자인을 사용하여 일반 크기의 원형 이미지와 함께 텍스트를 추가할 수도 있습니다. 텍스트는 잘라내기 전에 베젤의 거의 180도를 채울 수 있습니다.
>




-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/BezelCircularText_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/BezelCircularText_2x.png)

Closed gauge image


As you design images for a regular-size circular complication, use the following values for guidance.
> 정규 크기의 원형 합병증에 대한 이미지를 설계할 때 다음 값을 지침으로 사용하십시오.
>




| Image | 40mm | 41mm | 44mm | 45mm/49mm |
| --- | --- | --- | --- | --- |
| Image | 42x42 pt (84x84 px @2x) | 44.5x44.5 pt (89x89 px @2x) | 47x47 pt (94x94 px @2x) | 50x50 pt (100x100 px @2x) |
| Closed gauge | 27x27 pt (54x54 px @2x) | 28.5x28.5 pt (57x57 px @2x) | 31x31 pt (62x62 px @2x) | 32x32 pt (64x64 px @2x) |
| Open gauge | 11x11 pt (22x22 px @2x) | 11.5x11.5 pt (23x23 px @2x) | 12x12 pt (24x24 px @2x) | 13x13 pt (26x26 px @2x) |
| Stack (not text) | 28x14 pt (56x28 px @2x) | 29.5x15 pt (59X30 px @2x) | 31x16 pt (62x32px @ 2x) | 33.5x16.5 pt (67x33 px @2x) |

**NOTE**The system applies a circular mask to each image.
> 참고 시스템은 각 이미지에 원형 마스크를 적용합니다.
>




A SwiftUI view that implements a regular-size circular complication uses the following default text values:
> 정규 크기 원형 복잡도를 구현하는 SwiftUI 보기는 다음과 같은 기본 텍스트 값을 사용합니다.
>




- Style: Rounded
- Weight: Medium
- Text size: 12pt (40mm), 12.5pt (41mm), 13pt (44mm), 14.5pt (45mm/49mm)
- >  문자크기 : 12pt(40mm), 12.5pt(41mm), 13pt(44mm), 14.5pt(45mm/49mm)


If you want to design an oversized treatment of important information that can appear on the X-Large watch face — for example, the Contacts complication, which features a contact photo — use the extra-large versions of the circular family’s layouts. The following layouts let you display full-color images, text, and gauges in a large circular region that fills most of the X-Large watch face. Some of the text fields can support multicolor text.
> 초대형 워치페이스에 표시될 수 있는 중요한 정보(예: 연락처 사진이 포함된 연락처 합병증)에 대한 과도한 처리를 설계하려면 원형 패밀리 레이아웃의 초대형 버전을 사용합니다. 다음 레이아웃을 사용하면 X-Large 워치 페이스의 대부분을 채우는 큰 원형 영역에 풀 컬러 이미지, 텍스트 및 게이지를 표시할 수 있습니다. 일부 텍스트 필드는 다색 텍스트를 지원할 수 있습니다.
>




-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-xl-circular-closed-gauge-image_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-xl-circular-closed-gauge-image_2x.png)

Closed gauge image

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-xl-circular-closed-gauge-text_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-xl-circular-closed-gauge-text_2x.png)

Closed gauge text

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-xl-circular-open-gauge-image_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-xl-circular-open-gauge-image_2x.png)

Open gauge image

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-xl-circular-open-gauge-simple-text_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-xl-circular-open-gauge-simple-text_2x.png)

Open gauge text

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-xl-circular-open-gauge-range-text_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-xl-circular-open-gauge-range-text_2x.png)

Open gauge range

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-xl-circular-image_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-xl-circular-image_2x.png)

Image

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-xl-circular-stack-image_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-xl-circular-stack-image_2x.png)

Stack image

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-xl-circular-stack-text_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/complication-graphic-xl-circular-stack-text_2x.png)

Stack text


Use the following values for guidance as you create images for an extra-large circular complication.
> 초대형 원형 합병증에 대한 영상을 만들 때 다음 값을 지침으로 사용합니다.
>




| Image | 40mm | 41mm | 44mm | 45mm/49mm |
| --- | --- | --- | --- | --- |
| Image | 120x120 pt (240x240 px @2x) | 127x127 pt (254x254 px @2x) | 132x132 pt (264x264 px @2x) | 143x143 pt (286x286 px @2x) |
| Open gauge | 31x31 pt (62x62 px @2x) | 33x33 pt (66x66 px @2x) | 33x33 pt (66x66 px @2x) | 37x37 pt (74x74 px @2x) |
| Closed gauge | 77x77 pt (154x154 px @2x) | 81.5x81.5 (163x163 px @2x) | 87x87 pt (174x174 px @2x) | 91.5x91.5 (183x183 px @2x) |
| Stack | 80x40 pt (160x80 px @2x) | 85x42 (170x84 px @2x) | 87x44 pt (174x88 px @2x) | 95x48 pt (190x96 px @2x ) |

**NOTE**The system applies a circular mask to the circular, open-gauge, and closed-gauge images.
> 참고 시스템은 원형, 오픈 게이지 및 클로즈드 게이지 영상에 원형 마스크를 적용합니다.
>




Use the following values to create no-content placeholder images for your circular-family complications.
> 다음 값을 사용하여 순환 패밀리 합병증에 대한 내용 없는 자리 표시자 이미지를 만듭니다.
>




| Layout | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
| --- | --- | --- | --- | --- | --- |
| Circular | – | 42x42 pt (84x84 px @2x) | 44.5x44.5 pt (89x89 px @2x) | 47x47 pt (94x94 px @2x) | 50x50 pt (100x100 px @2x) |
| Bezel | – | 42x42 pt (84x84 px @2x) | 44.5x44.5 pt (89x89 px @2x) | 47x47 pt (94x94 px @2x) | 50x50 pt (100x100 px @2x) |
| Extra Large | – | 120x120 pt (240x240 px @2x) | 127x127 pt (254x254 px @2x) | 132x132 pt (264x264 px @2x) | 143x143 pt (286x286 px @2x) |

A SwiftUI view that implements an extra-large circular layout uses the following default text values:
> 초대형 원형 레이아웃을 구현하는 SwiftUI 보기는 다음과 같은 기본 텍스트 값을 사용합니다.
>




- Style: Rounded
- Weight: Medium
- Text size: 34.5pt (40mm), 36.5pt (41mm), 36.5pt (44mm), 41pt (45mm/49mm)
- >  문자크기 : 34.5pt(40mm), 36.5pt(41mm), 36.5pt(44mm), 41pt(45mm/49mm)


# **Corner**

Corner layouts let you display full-color images, text, and gauges in the corners of the watch face, like Infograph. Some of the templates also support multicolor text.
> 모서리 레이아웃을 사용하면 인포그래프와 같이 시계 면의 모서리에 전체 색상 이미지, 텍스트 및 게이지를 표시할 수 있습니다. 일부 템플릿은 다색 텍스트도 지원합니다.
>




-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CornerCircularImage_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CornerCircularImage_2x.png)

Circular image

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CornerGaugeImage_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CornerGaugeImage_2x.png)

Gauge image

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CornerGaugeText_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CornerGaugeText_2x.png)

Gauge text

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CornerStackText_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CornerStackText_2x.png)

Stack text

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CornerTextImage_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications/images/CornerTextImage_2x.png)

Text image


As you design images for a corner complication, use the following values for guidance.
> 모서리 합병증에 대한 영상을 설계할 때 다음 값을 지침으로 사용하십시오.
>




| Image | 40mm | 41mm | 44mm | 45mm/49mm |
| --- | --- | --- | --- | --- |
| Circular | 32x32 pt (64x64 px @2x) | 34x34 pt (68x68 px @2x) | 36x36 pt (72x72 px @2x) | 38x38 pt (76x76 px @2x ) |
| Gauge | 20x20 pt (40x40 px @2x) | 21x21 pt (42x42 px @2x) | 22x22 pt (44x44 px @2x) | 24x24 pt (48x48 px @2x) |
| Text | 20x20 pt (40x40 px @2x) | 21x21 pt (42x42 px @2x) | 22x22 pt (44x44 px @2x) | 24x24 pt (48x48 px @2x) |

**NOTE**The system applies a circular mask to each image.
> 참고 시스템은 각 이미지에 원형 마스크를 적용합니다.
>




