# **[components-status] top-shelf**

## The Apple TV Home Screen provides an area called Top Shelf, which showcases your content in a rich, engaging way while also giving people access to their favorite apps in the Dock.
> Apple TV 홈 스크린은 상단 선반이라고 불리는 영역을 제공하며, 이 영역은 사용자의 콘텐츠를 풍부하고 매력적인 방식으로 보여주는 동시에 사람들이 독에서 가장 좋아하는 앱에 액세스할 수 있도록 해줍니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/top-shelf-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/top-shelf-intro-dark_2x.png)

When you support full-screen Top Shelf, people can swipe through multiple full-screen content views, play trailers and previews, and get more information about your content.
> 전체 화면 상단 선반을 지원하는 경우 사용자는 여러 개의 전체 화면 콘텐츠 보기를 훑어보고, 트레일러 및 미리 보기를 재생하고, 콘텐츠에 대한 자세한 정보를 얻을 수 있습니다.
>




Top Shelf is a unique opportunity to highlight new, featured, or recommended content and let people jump directly to your app or game to view it. For example, when people select Apple TV in the Dock, full-screen previews immediately begin playing and soon the Dock slides away. As people watch previews for the first show, they can swipe through previews of all other featured shows, stopping to select Play or More Info for a preview that interests them.
> 상단 쉘프는 새로운 콘텐츠, 기능 또는 추천 콘텐츠를 강조 표시하고 사용자가 직접 앱 또는 게임으로 이동하여 볼 수 있는 고유한 기회입니다. 예를 들어, 독에서 Apple TV를 선택하면 전체 화면 미리 보기가 즉시 재생되기 시작하고 곧 독이 사라집니다. 사람들이 첫 번째 쇼의 미리 보기를 볼 때 다른 모든 특집 쇼의 미리 보기를 스와이프하여 관심 있는 미리 보기를 위해 재생 또는 추가 정보를 선택할 수 있습니다.
>




The system defines several layout templates that you can use to give people a compelling Top Shelf experience when they select your app in the Dock. To help you position content, you can download these templates from [Apple Design Resources](https://developer.apple.com/design/resources/#tvos-apps).
> 이 시스템은 사용자가 독에서 앱을 선택할 때 사람들에게 매력적인 상단 선반 경험을 제공하는 데 사용할 수 있는 몇 가지 레이아웃 템플릿을 정의합니다. 내용을 쉽게 배치할 수 있도록 Apple Design Resources에서 이러한 템플릿을 다운로드할 수 있습니다.
>




# **Best practices**

**Help people jump right into your content.** Top Shelf provides a path to the content people care about most. Two of the system-provided layout templates — [carousel actions](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf#carousel-actions) and [carousel details](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf#carousel-details) — each include two buttons by default: A primary button intended to begin playback and a More Info button intended to open your app to a view that displays details about the content.
> 다른 사용자가 콘텐츠로 바로 이동할 수 있도록 도와줍니다. 상단 선반은 사용자가 가장 관심을 갖는 콘텐츠에 대한 경로를 제공합니다. 시스템에서 제공하는 레이아웃 템플릿 중 두 개(카루셀 동작 및 카루셀 세부 정보)에는 각각 기본적으로 두 개의 버튼이 있습니다. 재생을 시작하는 기본 버튼과 콘텐츠에 대한 세부 정보를 표시하는 보기로 앱을 여는 추가 정보 버튼입니다.
>




**Feature new content.** For example, showcase new releases or episodes, highlight upcoming movies and shows, and avoid promoting content that people have already purchased, rented, or watched.
> 새로운 콘텐츠를 제공합니다. 예를 들어, 새로운 개봉작이나 에피소드를 보여주고, 다가오는 영화와 쇼를 강조하며, 사람들이 이미 구입했거나, 대여했거나, 또는 시청한 콘텐츠를 홍보하지 않도록 합니다.
>




**Personalize people’s favorite content.** People typically put the apps they use most often into Top Shelf. You can personalize their experience by showing targeted recommendations in the Top Shelf content you supply, letting people resume media playback or jump back into active gameplay.
> 사람들이 가장 좋아하는 콘텐츠를 개인화합니다. 사람들은 일반적으로 가장 자주 사용하는 앱을 맨 위 선반에 넣습니다. 사용자가 제공하는 상단 선반 콘텐츠에 대상 추천을 표시하여 사용자가 미디어 재생을 다시 시작하거나 활성 게임플레이로 다시 뛰어들 수 있도록 함으로써 사용자의 경험을 개인화할 수 있습니다.
>




**Avoid showing advertisements or prices.** People put your app into Top Shelf because you’ve already sold them on it, so they may not appreciate seeing lots of ads from your app. Showing purchasable content in the Top Shelf is fine, but prefer putting the focus on new and exciting content, and consider displaying prices only when people show interest.
> 광고나 가격을 표시하는 것을 피하십시오. 앱을 이미 판매했기 때문에 앱에서 많은 광고를 보는 것을 좋아하지 않을 수 있습니다. 상단 선반에 구매 가능한 콘텐츠를 보여주는 것도 좋지만 새롭고 흥미로운 콘텐츠에 초점을 맞추는 것을 선호하고, 사람들이 관심을 보일 때만 가격 표시를 고려한다.
>




**Showcase compelling dynamic content.** The videos and images you show in the Top Shelf should draw people in and encourage them to view more. If necessary, you can supply static images, but people typically prefer a captivating, dynamic Top Shelf experience that features the newest or highest rated content. To provide this experience, prefer creating [layered images](https://developer.apple.com/design/human-interface-guidelines/foundations/images/#layered-images) to display in Top Shelf.
> 매력적인 역동적인 콘텐츠를 선보입니다. 상단 선반에 표시된 비디오와 이미지는 사람들을 끌어들여 더 많이 보도록 장려해야 합니다. 필요한 경우 정적 이미지를 제공할 수 있지만, 일반적으로 최신 또는 최고 등급의 콘텐츠를 제공하는 매력적이고 동적인 탑 셸프 경험을 선호합니다. 이러한 환경을 제공하려면 맨 위 선반에 표시할 계층화된 이미지를 만드는 것이 좋습니다.
>




**If you don't provide the recommended full-screen content, supply at least one static image as a fallback.** The system displays a static image when your app is in the Dock and in focus and full-screen content is unavailable. tvOS flips and blurs the image, ensuring that it fits into a width of 1920 pixels at the 16:9 aspect ratio. Use the following values for guidance.
> 권장되는 전체 화면 콘텐츠를 제공하지 않는 경우 정적 이미지를 하나 이상 폴백으로 제공하십시오. 앱이 도킹에 있고 포커스가 있고 전체 화면 콘텐츠를 사용할 수 없을 때 시스템에서 정적 이미지를 표시합니다. tvOS는 이미지를 뒤집고 흐리게 하여 16:9 가로 세로 비율로 1920픽셀의 너비에 맞도록 합니다. 지침으로 다음 값을 사용하십시오.
>




| Image size (@1x) | Image size (@2x) |
| --- | --- |
| 2320px × 720px (2320pt × 720pt @1x) | 4640px × 1440px (2320pt × 720pt @2x) |

**Avoid implying interactivity in a static image.** A static Top Shelf image isn’t focusable, and you don’t want to make people think it’s interactive.
> 정적 이미지에 상호 작용을 암시하지 않도록 합니다. 정적 상위 선반 이미지는 초점을 맞출 수 없으므로 사람들이 상호 작용적이라고 생각하지 않도록 해야 합니다.
>




# **Dynamic layouts**

Dynamic Top Shelf imagery can appear in several ways:
> 동적 탑 쉘프 이미지는 다음과 같은 여러 가지 방법으로 표시될 수 있습니다.
>




- A carousel of full-screen video and images that includes two buttons and optional details
- >  두 개의 버튼과 선택적 세부 정보가 포함된 전체 화면 비디오 및 이미지의 회전목마

- A row of focusable content
- >  집중할 수 있는 콘텐츠의 행

- A set of scrolling banners
- >  스크롤 배너 세트


# **Carousel actions**

The carousel actions layout style focuses on full-screen video and images and includes a few unobtrusive controls that help people see more. This layout style works especially well to showcase content that people already know something about. For example, it's great for displaying user-generated content, like photos, or new content from a franchise or show that people are likely to enjoy.
> 회전식 액션 레이아웃 스타일은 전체 화면 비디오와 이미지에 초점을 맞추고 사람들이 더 많이 볼 수 있도록 도와주는 몇 가지 눈에 띄지 않는 컨트롤을 포함한다. 이러한 레이아웃 스타일은 사람들이 이미 알고 있는 콘텐츠를 보여주기 위해 특히 잘 작동합니다. 예를 들어, 사진과 같은 사용자 생성 콘텐츠나 프랜차이즈의 새로운 콘텐츠 또는 사람들이 즐길 수 있는 쇼를 표시하는 데 적합합니다.
>




**Provide a title.** Include a succinct title, like the title of the show or movie or the title of a photo album. If necessary, you can also provide a brief subtitle. For example, a subtitle for a photo album could be a range of dates; a subtitle for an episode could be the name of the show.
> 제목을 제공합니다. 프로그램이나 영화 제목 또는 사진 앨범 제목과 같은 간결한 제목을 포함합니다. 필요한 경우 간단한 부제를 제공할 수도 있습니다. 예를 들어, 사진 앨범의 부제는 날짜 범위일 수 있고, 에피소드의 부제는 프로그램 이름일 수 있습니다.
>




# **Carousel details**

This layout style extends the carousel actions layout style, giving you the opportunity to include some information about the content. For example, you might provide information like a plot summary, cast list, and other metadata that helps people decide whether to choose the content.
> 이 레이아웃 스타일은 캐러셀 동작 레이아웃 스타일을 확장하여 내용에 대한 일부 정보를 포함할 수 있습니다. 예를 들어, 내용 선택 여부를 결정하는 데 도움이 되는 플롯 요약, 캐스트 목록 및 기타 메타데이터와 같은 정보를 제공할 수 있습니다.
>




**Provide a title that identifies the currently playing content.** The content title appears near the top of the screen so it's easy for people to read it at a glance. Above the title, you can also provide a succinct phrase or app attribution, like "Featured on *My App*."
> 현재 재생 중인 콘텐츠를 식별할 수 있는 제목을 제공합니다. 콘텐츠 제목은 화면 상단 근처에 표시되므로 한 눈에 쉽게 볼 수 있습니다. 제목 위에 "내 앱에 기능"과 같은 간결한 문구나 앱 속성을 제공할 수도 있습니다.
>




# **Sectioned content row**

This layout style shows a single labeled row of sectioned content, which can work well to highlight recently viewed content, new content, or favorites. Row content is focusable, which lets people scroll quickly through it. A label appears when an individual piece of content comes into focus, and small movements on the remote’s Touch surface bring the focused image to life. You can also configure a sectioned content row to show multiple labels.
> 이 레이아웃 스타일은 최근에 본 내용, 새 내용 또는 즐겨찾기를 강조 표시하는 데 적합한 섹션 내용의 단일 레이블 행을 표시합니다. 행 내용은 포커스가 가능하여 사용자가 빠르게 스크롤할 수 있습니다. 라벨은 개별 콘텐츠에 초점이 맞춰지면 나타나며 리모컨의 터치 표면에서 작은 움직임을 통해 초점이 맞춰진 이미지에 생기를 불어넣습니다. 여러 레이블을 표시하도록 섹션화된 내용 행을 구성할 수도 있습니다.
>




**Provide enough content to constitute a complete row.** At a minimum, load enough images in a sectioned content row to span the full width of the screen. In addition, include at least one label for greater platform consistency and to provide additional context.
> 전체 행을 구성할 수 있는 충분한 콘텐츠를 제공하십시오. 최소한 화면의 전체 너비에 걸쳐 섹션화된 콘텐츠 행에 충분한 이미지를 로드하십시오. 또한 플랫폼 일관성을 높이고 추가 컨텍스트를 제공하기 위해 하나 이상의 레이블을 포함하십시오.
>




You can use the following image sizes in a sectioned content row.
> 섹션된 내용 행에서 다음 이미지 크기를 사용할 수 있습니다.
>




### **Poster (2:3)**

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf/images/icons-and-images-content-layout-2x3-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf/images/icons-and-images-content-layout-2x3-dark_2x.png)

| Aspect | Image size (@1x) | Image size (@2x) |
| --- | --- | --- |
| Actual size | 404px × 608px (404pt × 608pt @1x) | 808px × 1216px (404pt × 608pt @2x) |
| Focused/Safe zone size | 380px × 570px (380pt × 570pt @1x) | 760px × 1140px (380pt × 570pt @2x) |
| Unfocused size | 333px × 570px (333pt × 570pt @1x) | 666px × 1140px (333pt × 570pt @2x) |

### **Square (1:1)**

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf/images/icons-and-images-content-layout-1x1-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf/images/icons-and-images-content-layout-1x1-dark_2x.png)

| Aspect | Image size (@1x) | Image size (@2x) |
| --- | --- | --- |
| Actual size | 608px × 608px (608pt × 608pt @1x) | 1216px × 1216px (608pt × 608pt @2x) |
| Focused/Safe zone size | 570px × 570px (570pt × 570pt @1x) | 1140px × 1140px (570pt × 570pt @2x) |
| Unfocused size | 500px × 500px (500pt × 500pt @1x) | 1000px × 1000px (500pt × 500pt @2x) |

### **16:9**

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf/images/icons-and-images-content-layout-16x9-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf/images/icons-and-images-content-layout-16x9-dark_2x.png)

| Aspect | Image size (@1x) | Image size (@2x) |
| --- | --- | --- |
| Actual size | 908px × 512px (908pt × 512pt @1x) | 1816px × 1024px (908pt × 512pt @2x) |
| Focused/Safe zone size | 852px × 479px (852pt × 479pt @1x) | 1704px × 958px (852pt × 479pt @2x) |
| Unfocused size | 782px × 440px (782pt × 440pt @1x) | 1564px × 880px (782pt × 440pt @2x) |

**Be aware of additional scaling when combining image sizes.** If your Top Shelf design includes a mixture of image sizes, keep in mind that images will automatically scale up to match the height of the tallest image if necessary. For example, a 16:9 image scales to 500 pixels high if included in a row with a poster or square image.
> 이미지 크기를 결합할 때 추가적인 크기 조정에 유의하십시오. 상단 선반 설계에 이미지 크기가 혼합된 경우 필요한 경우 이미지가 가장 높은 이미지의 높이에 맞게 자동으로 크기 조정됩니다. 예를 들어, 포스터나 사각형 이미지가 있는 행에 포함된 경우 16:9 이미지는 500픽셀 높이로 확장됩니다.
>




### **Scrolling inset banner**

This layout shows a series of large images, each of which spans almost the entire width of the screen. Apple TV automatically scrolls through these banners on a preset timer until people bring one into focus. The sequence circles back to the beginning after the final image is reached.
> 이 레이아웃은 각 이미지가 화면의 거의 전체 너비에 걸쳐 있는 일련의 큰 이미지를 보여줍니다. 애플 TV는 사람들이 배너에 초점을 맞출 때까지 자동으로 미리 설정된 타이머로 배너를 스크롤합니다. 시퀀스는 최종 영상에 도달한 후 처음으로 원을 그리며 돌아갑니다.
>




When a banner is in focus, a small, circular gesture on the remote’s Touch surface enacts the system focus effect, animating the item, applying lighting effects, and, if the banner contains layered images, producing a 3D effect. Swiping on the Touch surface pans to the next or previous banner in the sequence. Use this style to showcase rich, captivating content, such as a popular new movie.
> 배너가 포커스에 있을 때 리모컨의 터치 표면에 있는 작고 원형 제스처는 시스템 포커스 효과를 구현하여 항목을 애니메이션화하고 조명 효과를 적용하며 배너에 레이어드 이미지가 포함된 경우 3D 효과를 생성합니다. 터치 표면을 스와이프하면 다음 또는 이전 배너로 이동합니다. 이 스타일을 사용하여 인기 있는 새 영화와 같은 풍부하고 매혹적인 콘텐츠를 보여줍니다.
>




**Provide three to eight images.** A minimum of three images is recommended for a scrolling banner to feel effective. More than eight images can make it hard to navigate to a specific image.
> 3~8개의 이미지를 제공합니다. 스크롤 배너가 효과적으로 느껴지려면 최소 3개의 이미지를 사용하는 것이 좋습니다. 이미지가 8개 이상이면 특정 이미지로 이동하기 어려울 수 있습니다.
>




**If you need text, add it to your image.** This layout style doesn’t show labels under content, so all text must be part of the image itself. In layered images, consider elevating text by placing it on a dedicated layer above the others. Add the text to the accessibility label of the image too, so [VoiceOver](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility#voiceover)can read it.
> 텍스트가 필요한 경우 이미지에 추가하십시오. 이 레이아웃 스타일은 내용 아래에 레이블을 표시하지 않으므로 모든 텍스트가 이미지의 일부여야 합니다. 레이어드된 이미지에서는 텍스트를 다른 레이어 위의 전용 레이어에 배치하여 높이는 것을 고려하십시오. VoiceOver가 읽을 수 있도록 이미지의 내게 필요한 옵션 레이블에도 텍스트를 추가합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf/images/icons-and-images-content-layout-extra-wide_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/top-shelf/images/icons-and-images-content-layout-extra-wide_2x.png)

Use the following size for a scrolling inset banner image:
> 설정된 배너 이미지에서 스크롤하려면 다음 크기를 사용합니다.
>




| Aspect | Image size (@1x) | Image size (@2x) |
| --- | --- | --- |
| Actual size | 1940px × 692px (1940pt × 692pt @1x) | 3880px × 1384px (1940pt × 692pt @2x) |
| Focused/Safe zone size | 1740px × 620px (1740pt × 620pt @1x) | 3480px × 1240px (1740pt × 620pt @2x) |
| Unfocused size | 1740px × 560px (1740pt × 560pt @1x) | 3480px × 1120px (1740pt × 560pt @2x) |
