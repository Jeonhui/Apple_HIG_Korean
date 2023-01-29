# **[technologies] live-photos**

# Live Photos lets people capture favorite memories in a sound- and motion-rich interactive experience that adds vitality to traditional still photos.
> 라이브 포토는 사람들이 소리와 움직임이 풍부한 대화형 경험으로 좋아하는 기억을 캡처할 수 있게 해주며, 이는 기존의 스틸 사진에 활력을 더해줍니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Live-Photos-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Live-Photos-intro_2x.png)

When Live Photos is enabled, the Camera app captures additional content — including audio and extra frames — before and after people take a photo. People press a Live Photo to see it spring to life.
> 라이브 사진이 활성화되면 카메라 앱은 사람들이 사진을 찍기 전과 찍은 후에 오디오 및 추가 프레임을 포함한 추가 콘텐츠를 캡처합니다. 사람들은 그것이 살아나는 것을 보기 위해 라이브 포토를 누릅니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/live-photos/images/Live_Photos_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/live-photos/images/Live_Photos_2x.png)

Play

**Apply adjustments to all frames.** If your app lets people apply effects or adjustments to a Live Photo, make sure those changes are applied to the entire photo. If you don’t support this, give people the option of converting it to a still photo.
> 모든 프레임에 조정을 적용합니다. 앱에서 실시간 사진에 효과 또는 조정을 적용할 수 있는 경우 변경 사항이 전체 사진에 적용되는지 확인하십시오. 이 기능을 지원하지 않는 경우 사용자에게 스틸 사진으로 변환할 수 있는 옵션을 제공합니다.
>




**Keep Live Photo content intact.** It’s important for people to experience Live Photos in a consistent way that uses the same visual treatment and interaction model across all apps. Don’t disassemble a Live Photo and present its frames or audio separately.
> 실시간 사진 콘텐츠를 그대로 유지합니다. 모든 앱에서 동일한 시각적 처리 및 상호 작용 모델을 사용하는 일관된 방식으로 실시간 사진을 경험하는 것이 중요합니다. 라이브 사진을 분해하여 프레임이나 오디오를 별도로 표시하지 마십시오.
>




**Implement a great photo sharing experience.** If your app supports photo sharing, let users preview the entire contents of Live Photos before deciding to share. Always offer the option to share Live Photos as traditional photos.
> 훌륭한 사진 공유 환경을 구현하십시오. 앱에서 사진 공유를 지원하는 경우 사용자가 공유를 결정하기 전에 라이브 사진의 전체 내용을 미리 볼 수 있습니다. 항상 라이브 사진을 기존 사진으로 공유할 수 있는 옵션을 제공합니다.
>




**Clearly indicate when a Live Photo is downloading and when the photo is playable.** Show a progress indicator during the download process and provide some indication when the download is complete.
> 라이브 사진이 다운로드되는 시간과 사진이 재생 가능한 시간을 명확히 표시합니다. 다운로드 프로세스 중에 진행률 표시기를 표시하고 다운로드가 완료되면 몇 가지 표시를 제공합니다.
>




**Display Live Photos as traditional photos in environments that don’t support Live Photos.**Don’t attempt to replicate the Live Photos experience provided in a supported environment. Instead, show a traditional, still representation of the photo.
> 라이브 사진을 지원하지 않는 환경에서는 라이브 사진을 기존 사진으로 표시합니다.지원되는 환경에서 제공되는 라이브 사진 환경을 복제하지 마십시오. 대신, 전통적이고 스틸 사진을 보여주세요.
>




**Make Live Photos easily distinguishable from still photos.** The best way to identify a Live Photo is through a hint of movement. Note that there are no built-in Live Photo motion effects, like the one that occurs as you swipe through photos in the full-screen browser of Photos app. Any motion effects like this must be custom designed and implemented. In cases where movement isn’t possible, show a system-provided badge above the photo. This badge can be displayed as an overlay with a shadow or as a solid color without a shadow. A badge variant is also available for situations where a Live Photo appears as a traditional photo. Never include a playback button that could be interpreted as a video playback button.
> 실시간 사진과 스틸 사진을 쉽게 구분할 수 있도록 합니다. 실시간 사진을 식별하는 가장 좋은 방법은 약간의 움직임을 통해서입니다. 사진 앱의 전체 화면 브라우저에서 사진을 스와이프할 때 발생하는 것과 같은 기본 제공 라이브 사진 모션 효과는 없습니다. 이와 같은 모든 모션 효과는 사용자 지정 설계 및 구현되어야 합니다. 이동할 수 없는 경우 사진 위에 시스템에서 제공한 배지를 표시합니다. 이 배지는 그림자가 있는 오버레이 또는 그림자가 없는 단색으로 표시될 수 있습니다. 라이브 사진이 기존 사진으로 나타나는 상황에 대해서도 배지 변형을 사용할 수 있습니다. 비디오 재생 버튼으로 해석될 수 있는 재생 버튼은 포함하지 마십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/live-photos/images/Live_BadgeA_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/live-photos/images/Live_BadgeA_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/live-photos/images/Live_BadgeB_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/live-photos/images/Live_BadgeB_2x.png)

**Keep badge placement consistent.** If you show a badge, put it in the same location on every photo. Typically, a badge looks best in a corner of a photo.
> 배지 배치를 일정하게 유지합니다. 배지를 표시할 경우 모든 사진의 동일한 위치에 배치하십시오. 일반적으로 배지는 사진의 한 구석에 가장 잘 나타납니다.
>



