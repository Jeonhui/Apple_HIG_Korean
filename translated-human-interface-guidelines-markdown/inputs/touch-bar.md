### [[Inputs](./translated-human-interface-guidelines-markdown/inputs.md)]  
  
# **Touch Bar**  

Important



By default, the system APIs return SF Symbols configured as 13 pt, large scale, and medium weight.

> 기본적으로 시스템 API는 13pt, 대형 및 중중량으로 구성된 SF 심볼을 반환합니다.
>



In some cases, a symbol might not have the same size or alignment as the image it replaces, so it’s important to check your layout.

> 경우에 따라 심볼이 대체하는 이미지와 동일한 크기 또는 정렬을 갖지 않을 수 있으므로 레이아웃을 확인하는 것이 중요합니다.
>



**Prefer system images because people are familiar with them.** Also, system-provided glyphs automatically receive appropriate coloring, respond to system white-point changes based on factors such as ambient light and keyboard backlight level, and respond to user interactions.

> **사람들이 시스템 이미지에 익숙하기 때문에 시스템 이미지를 선호합니다.** 또한, 시스템 제공 글리프는 자동으로 적절한 색상을 제공받고, 주변광 및 키보드 백라이트 레벨과 같은 요소에 기초한 시스템 화이트포인트 변화에 대응하며, 사용자 상호작용에 대응한다.
>



**Use each system-defined glyph according to its meaning — not its appearance.** When you choose an image for its meaning, your app can remain visually consistent with the system even if the appearance of the image changes.

> **각 시스템 정의 글리프를 외관이 아닌 의미에 따라 사용하십시오.** 이미지의 의미를 선택하면 이미지의 모양이 변경되더라도 앱이 시각적으로 시스템과 일치할 수 있습니다.
>



**Use only system images that are designed for the Touch Bar.** Don’t use other types of images in the Touch Bar, such as toolbar glyphs.

> **터치 바용으로 설계된 시스템 이미지만 사용하십시오.** 도구 모음 글리프와 같은 다른 유형의 이미지를 터치 바에서 사용하지 마십시오.
>



**Design a custom symbol or image if you can’t find a system-defined one that meets your needs.** Designing a custom symbol or image lets you communicate unique details that help people use your app; repurposing a system-defined image can cause confusion. For guidance, see [Custom Touch Bar icons](/design/human-interface-guidelines/touch-bar#Custom-Touch-Bar-icons)

> **필요에 맞는 시스템 정의 기호 또는 이미지를 찾을 수 없는 경우 사용자 정의 기호 또는 이미지를 설계합니다.** 사용자 지정 기호 또는 이미지를 설계하면 사용자가 앱을 사용하는 데 도움이 되는 고유한 세부 정보를 전달할 수 있습니다. 시스템 정의 이미지를 용도 변경하면 혼란이 발생할 수 있습니다. 자세한 내용은 [사용자 지정 터치 바 아이콘](/디자인/인간-인터페이스-가이드라인/터치 바#사용자 지정 터치 바 아이콘)을 참조하십시오
>

; for general design guidance, see [Icons](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/icons)

> ; 일반 설계 지침은 [Icons](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/icons) 를 참조하십시오
>

.



Note



Some system icons, like Go Back and Go Forward, automatically reverse direction in right-to-left locales.

> 뒤로 가기 및 앞으로 가기와 같은 일부 시스템 아이콘은 오른쪽에서 왼쪽으로 이동할 때 자동으로 방향을 반대로 전환합니다.
>







| Image (Catalina and earlier) | SF Symbol (macOS 11 and later) | Meaning |

| --- | --- | --- |

| A white plus sign within a black disk. [`touchBarAddDetailTemplateName`](/documentation/appkit/nsimage/2647000-touchbaradddetailtemplatename)

 |  plus.circle | Displays additional detail for an item. |

| A plus sign. [`touchBarAddTemplateName`](/documentation/appkit/nsimage/2544735-touchbaraddtemplatename)

 |  plus | Creates a new item. |

| An alarm clock with its hands at 9:00. [`touchBarAlarmTemplateName`](/documentation/appkit/nsimage/2646938-touchbaralarmtemplatename)

 |  alarm | Sets or displays an alarm. |

| A freestanding microphone with a slash through it. [`touchBarAudioInputMuteTemplateName`](/documentation/appkit/nsimage/2646941-touchbaraudioinputmutetemplatena)

 |  mic.slash | Mutes audio input or denotes that audio input is muted. |

| A freestanding microphone. [`touchBarAudioInputTemplateName`](/documentation/appkit/nsimage/2646933-touchbaraudioinputtemplatename)

 |  mic | Denotes audio input. |

| A right-facing speaker with 3 concentric curved lines representing sound waves. On top of the image is a slash from top left to bottom right. [`touchBarAudioOutputMuteTemplateName`](/documentation/appkit/nsimage/2646959-touchbaraudiooutputmutetemplaten)

 |  speaker.slash.fill | Mutes audio output or denotes that audio output is muted. |

| A right-facing speaker with 3 concentric curved lines representing sound waves. [`touchBarAudioOutputVolumeHighTemplateName`](/documentation/appkit/nsimage/2646973-touchbaraudiooutputvolumehightem)

 |  speaker.wave.3.fill | Sets the audio output volume to high or denotes that the audio output volume is set to high. |

| A right-facing speaker with 3 concentric curved lines representing sound waves. The outermost 2 waves are gray; the inner wave is black. [`touchBarAudioOutputVolumeLowTemplateName`](/documentation/appkit/nsimage/2646925-touchbaraudiooutputvolumelowtemp)

 |  speaker.wave.1.fill | Sets the audio output volume to low or denotes that the audio output volume is set to low. |

| A right-facing speaker with 3 concentric curved lines representing sound waves. The outermost wave is gray; the inner 2 waves are black. [`touchBarAudioOutputVolumeMediumTemplateName`](/documentation/appkit/nsimage/2646957-touchbaraudiooutputvolumemediumt)

 |  speaker.wave.2.fill | Sets the audio output volume to medium or denotes that the audio output volume is set to medium. |

| A right-facing speaker with 3 gray concentric curved lines representing sound waves. [`touchBarAudioOutputVolumeOffTemplateName`](/documentation/appkit/nsimage/2646988-touchbaraudiooutputvolumeofftemp)

 |  speaker.fill | Turns off audio output or denotes that audio output is turned off. |

| An open book. [`touchBarBookmarksTemplateName`](/documentation/appkit/nsimage/2646985-touchbarbookmarkstemplatename)

 |  book | Shows app-specific bookmarks. |

| A disk filled with wedges of rainbow colors. [`touchBarColorPickerFillName`](/documentation/appkit/nsimage/2646978-touchbarcolorpickerfillname)

 | – | Shows a color picker so people can select a fill color. |

| The letter A filled with rainbow colors. [`touchBarColorPickerFontName`](/documentation/appkit/nsimage/2646992-touchbarcolorpickerfontname)

 | – | Shows a color picker so people can select a text color. |

| A circle drawn with a stroke filled with rainbow colors. [`touchBarColorPickerStrokeName`](/documentation/appkit/nsimage/2646961-touchbarcolorpickerstrokename)

 | – | Shows a color picker so people can select a stroke color. |

| A solid black phone receiver. [`touchBarCommunicationAudioTemplateName`](/documentation/appkit/nsimage/2646979-touchbarcommunicationaudiotempla)

 |  phone | Initiates or denotes audio communication. |

| A solid black video camera. [`touchBarCommunicationVideoTemplateName`](/documentation/appkit/nsimage/2646932-touchbarcommunicationvideotempla)

 |  video | Initiates or denotes video communication. |

| An outlined square with a black pencil on top that goes from above the top-right corner to near the middle of the square. [`touchBarComposeTemplateName`](/documentation/appkit/nsimage/2544716-touchbarcomposetemplatename)

 |  square.and.pencil | Opens a new document or view in edit mode. |

| An outlined trash can. [`touchBarDeleteTemplateName`](/documentation/appkit/nsimage/2646939-touchbardeletetemplatename)

 |  trash | Deletes the current or selected item. |

| A white downward-pointing arrow within a black disk. [`touchBarDownloadTemplateName`](/documentation/appkit/nsimage/2646924-touchbardownloadtemplatename)

 |  arrow.down.circle | Downloads an item. |

| Two black arrows pointing away from each other. One arrow points to the bottom left and the other points to the top right. [`touchBarEnterFullScreenTemplateName`](/documentation/appkit/nsimage/2646946-touchbarenterfullscreentemplaten)

 |  arrow.up.left.and.arrow.down.right | Enters full screen mode. |

| Two black arrows pointing toward each other. One arrow points from the top right and the other points from the bottom left. [`touchBarExitFullScreenTemplateName`](/documentation/appkit/nsimage/2646983-touchbarexitfullscreentemplatena)

 |  arrow.down.right.and.arrow.up.left | Exits full screen mode. |

| Two black triangles both pointing right. [`touchBarFastForwardTemplateName`](/documentation/appkit/nsimage/2646994-touchbarfastforwardtemplatename)

 |  forward.fill | Fast-forwards through media playback or slides. |

| A black folder with a white square containing a black plus sign in the bottom-left corner. [`touchBarFolderCopyToTemplateName`](/documentation/appkit/nsimage/2646998-touchbarfoldercopytotemplatename)

 |  plus.rectangle.on.folder | Copies an item to a destination. |

| A black folder with a downward-pointing arrow on top of it. [`touchBarFolderMoveToTemplateName`](/documentation/appkit/nsimage/2646996-touchbarfoldermovetotemplatename)

 |  folder | Moves an item to a new destination. |

| A black folder. [`touchBarFolderTemplateName`](/documentation/appkit/nsimage/2646980-touchbarfoldertemplatename)

 |  folder | Opens or represents a folder. |

| A black, lowercase letter I within a black circle. [`touchBarGetInfoTemplateName`](/documentation/appkit/nsimage/2646951-touchbargetinfotemplatename)

 |  info.circle | Displays additional information about an item. |

| A left-pointing chevron. [`touchBarGoBackTemplateName`](/documentation/appkit/nsimage/2544848-touchbargobacktemplatename)

 |  chevron.backward | Returns to the previous screen or location. |

| A downward-pointing chevron. [`touchBarGoDownTemplateName`](/documentation/appkit/nsimage/2646945-touchbargodowntemplatename)

 |  chevron.down | Moves to the next vertical item. |

| A right-pointing chevron. [`touchBarGoForwardTemplateName`](/documentation/appkit/nsimage/2544734-touchbargoforwardtemplatename)

 |  chevron.forward | Moves to the next screen or location. |

| An upward-pointing chevron. [`touchBarGoUpTemplateName`](/documentation/appkit/nsimage/2646975-touchbargouptemplatename)

 |  chevron.up | Moves to the previous vertical item. |

| A clock that displays the time 9:00. [`touchBarHistoryTemplateName`](/documentation/appkit/nsimage/2646929-touchbarhistorytemplatename)

 |  clock | Displays historical information, such as recent downloads. |

| Two rows of three empty squares, each outlined in black. [`touchBarIconViewTemplateName`](/documentation/appkit/nsimage/2646943-touchbariconviewtemplatename)

 |  square.grid.2x2 | Displays items in an icon view. |

| A stack of four horizontal black lines. [`touchBarListViewTemplateName`](/documentation/appkit/nsimage/2646954-touchbarlistviewtemplatename)

 |  list.bullet | Displays items in a list view. |

| A closed black envelope with the flap outlined in white. [`touchBarMailTemplateName`](/documentation/appkit/nsimage/2646969-touchbarmailtemplatename)

 |  envelope | Creates an email message. |

| A black folder with a plus sign in the top-right corner. [`touchBarNewFolderTemplateName`](/documentation/appkit/nsimage/2646989-touchbarnewfoldertemplatename)

 |  folder.badge.plus | Creates a new folder. |

| A black message bubble. [`touchBarNewMessageTemplateName`](/documentation/appkit/nsimage/2646953-touchbarnewmessagetemplatename)

 |  message | Creates a new message or denotes the use of messaging. |

| A black compass needle pointing to north-east within a circle outlined in black. [`touchBarOpenInBrowserTemplateName`](/documentation/appkit/nsimage/2646990-touchbaropeninbrowsertemplatenam)

 |  safari | Opens an item in the browser. |

| Two vertical, parallel black bars. [`touchBarPauseTemplateName`](/documentation/appkit/nsimage/2646970-touchbarpausetemplatename)

 |  pause.fill | Pauses media playback or slides. Always store the current location when pausing, so playback can resume later. |

| A black, right-pointing triangle with two vertical parallel black bars on the right. [`touchBarPlayPauseTemplateName`](/documentation/appkit/nsimage/2646991-touchbarplaypausetemplatename)

 |  playpause.fill | Toggles between playing and pausing media or slides. |

| A black right-pointing triangle. [`touchBarPlayTemplateName`](/documentation/appkit/nsimage/2646967-touchbarplaytemplatename)

 |  play.fill | Begins or resumes media playback or slides. |

| A black eye shape with a white circle within it. [`touchBarQuickLookTemplateName`](/documentation/appkit/nsimage/2646952-touchbarquicklooktemplatename)

 |  eye | Opens an item in Quick Look. |

| A black disk. [`touchBarRecordStartTemplateName`](/documentation/appkit/nsimage/2646981-touchbarrecordstarttemplatename)

 |  circle.fill | Begins recording. |

| A black square. [`touchBarRecordStopTemplateName`](/documentation/appkit/nsimage/2646993-touchbarrecordstoptemplatename)

 |  stop.fill | Stops recording or stops media playback or slides. |

| A curved arrow indicating the clockwise direction. [`touchBarRefreshTemplateName`](/documentation/appkit/nsimage/2646995-touchbarrefreshtemplatename)

 |  arrow.clockwise | Moves backwards through media playback or slides. |

| Two black triangles both pointing left. [`touchBarRewindTemplateName`](/documentation/appkit/nsimage/2646950-touchbarrewindtemplatename)

 |  backward.fill | Moves backwards through media playback or slides. |

| A rectangle outlined in black with a curved, left-pointing arrow over the top-right corner. [`touchBarRotateLeftTemplateName`](/documentation/appkit/nsimage/2646972-touchbarrotatelefttemplatename)

 |  rotate.left | Moves to the next vertical item. |

| A rectangle outlined in black with a curved, right-pointing arrow over the top-left corner. [`touchBarRotateRightTemplateName`](/documentation/appkit/nsimage/2646977-touchbarrotaterighttemplatename)

 |  rotate.right | Rotates an item to the right. |

| A magnifying glass outlined in black, slanting to the left. [`touchBarSearchTemplateName`](/documentation/appkit/nsimage/2647001-touchbarsearchtemplatename)

 |  magnifyingglass | Displays a search field or initiates a search. |

| A square outlined in black with a black arrow pointing up from near the top edge. [`touchBarShareTemplateName`](/documentation/appkit/nsimage/2646948-touchbarsharetemplatename)

 |  square.and.arrow.up | Shares content with others or to social media. |

| A black-outlined rectangle divided by a vertical line about 40 percent from the left. Within the left side are a stack of three short, horizontal lines. [`touchBarSidebarTemplateName`](/documentation/appkit/nsimage/2646966-touchbarsidebartemplatename)

 |  sidebar.leading | Displays a sidebar in the current view. |

| The number 15 circled by a black double-headed arrow pointing right in a clockwise direction. [`touchBarSkipAhead15SecondsTemplateName`](/documentation/appkit/nsimage/2646930-touchbarskipahead15secondstempla)

 |  goforward.15 | Skips 15 seconds ahead during media playback. |

| The number 30 circled by a black double-headed arrow pointing right in a clockwise direction. [`touchBarSkipAhead30SecondsTemplateName`](/documentation/appkit/nsimage/2646927-touchbarskipahead30secondstempla)

 |  goforward.30 | Skips 30 seconds ahead during media playback. |

| Two black right-pointing triangles with a black vertical line at the point of the rightmost triangle. [`touchBarSkipAheadTemplateName`](/documentation/appkit/nsimage/2646974-touchbarskipaheadtemplatename)

 |  forward.end.alt.fill | Skips to the next chapter or location during media playback. |

| The number 15 circled by a black double-headed arrow pointing left in a counter clockwise direction. [`touchBarSkipBack15SecondsTemplateName`](/documentation/appkit/nsimage/2646934-touchbarskipback15secondstemplat)

 |  gobackward.15 | Skips 15 seconds back during media playback. |

| The number 30 circled by a double-headed black arrow pointing left in a counter clockwise direction. [`touchBarSkipBack30SecondsTemplateName`](/documentation/appkit/nsimage/2646976-touchbarskipback30secondstemplat)

 |  gobackward.30 | Skips 30 seconds back during media playback. |

| Two black left-pointing triangles with a black vertical line at the point of the leftmost triangle. [`touchBarSkipBackTemplateName`](/documentation/appkit/nsimage/2646944-touchbarskipbacktemplatename)

 |  backward.end.alt.fill | Skips to the previous chapter or location during media playback. |

| A black right-pointing triangle with a vertical black line at the point. [`touchBarSkipToEndTemplateName`](/documentation/appkit/nsimage/2646956-touchbarskiptoendtemplatename)

 |  forward.end.fill | Skips to the end during media playback. |

| A black left-pointing triangle with a vertical black line at the point. [`touchBarSkipToStartTemplateName`](/documentation/appkit/nsimage/2646968-touchbarskiptostarttemplatename)

 |  backward.end.fill | Skips to the start during media playback. |

| A black right-pointing triangle within a black-outlined rectangle. [`touchBarSlideshowTemplateName`](/documentation/appkit/nsimage/2646935-touchbarslideshowtemplatename)

 |  play.rectangle | Starts a slideshow. |

| A tag outlined in black, pointing left. [`touchBarTagIconTemplateName`](/documentation/appkit/nsimage/2646958-touchbartagicontemplatename)

 |  tag | Applies a tag to an item. |

| The capital letter B drawn in a thick black stroke. [`touchBarTextBoldTemplateName`](/documentation/appkit/nsimage/2646964-touchbartextboldtemplatename)

 |  bold | Makes text bold. |

| A capital letter T within a square outlined in black. A black dot is at the center of both vertical sides of the square. [`touchBarTextBoxTemplateName`](/documentation/appkit/nsimage/2646963-touchbartextboxtemplatename)

 |  textbox | Inserts a text box. |

| A stack of four horizontal black lines. From the top, the first and third are one length and the second and fourth are a shorter length. The midpoint of each line is at the same horizontal position. [`touchBarTextCenterAlignTemplateName`](/documentation/appkit/nsimage/2646940-touchbartextcenteraligntemplaten)

 |  text.aligncenter | Center aligns text. |

| A black capital letter I slanted slightly to the right. [`touchBarTextItalicTemplateName`](/documentation/appkit/nsimage/2646942-touchbartextitalictemplatename)

 |  italic | Italicizes text. |

| A stack of four horizontal black lines all the same length. [`touchBarTextJustifiedAlignTemplateName`](/documentation/appkit/nsimage/2646962-touchbartextjustifiedaligntempla)

 |  text.justify | Justifies text, aligning it to both the left and right. |

| A stack of four horizontal black lines. From the top, the first and third are one length, the second and fourth are a shorter length. All four lines start from the same horizontal position on the left. [`touchBarTextLeftAlignTemplateName`](/documentation/appkit/nsimage/2646937-touchbartextleftaligntemplatenam)

 |  text.alignleft | Left-aligns text. |

| A stack of four horizontal lines of the same length, each with a black bullet on the left. [`touchBarTextListTemplateName`](/documentation/appkit/nsimage/2646960-touchbartextlisttemplatename)

 |  list.bullet | Inserts a list or converts text to list form. |

| A stack of four horizontal black lines. From the top, the first and third are one length, the second and fourth are a shorter length. All four lines start from the same horizontal position on the right. [`touchBarTextRightAlignTemplateName`](/documentation/appkit/nsimage/2646999-touchbartextrightaligntemplatena)

 |  text.alignright | Right-aligns text. |

| A capital letter S with a short horizontal line through the middle. [`touchBarTextStrikethroughTemplateName`](/documentation/appkit/nsimage/2646986-touchbartextstrikethroughtemplat)

 |  strikethrough | Applies a strikethrough to text. |

| A capital letter U sitting on a short horizontal line. [`touchBarTextUnderlineTemplateName`](/documentation/appkit/nsimage/2646947-touchbartextunderlinetemplatenam)

 |  underline | Underlines text. |

| The silhouette of a person’s head and shoulders within a circle. A small plus sign is on the right side of the silhouette. [`touchBarUserAddTemplateName`](/documentation/appkit/nsimage/2646936-touchbaruseraddtemplatename)

 |  person.crop.circle.badge.plus | Creates a new user. |

| The silhouettes of two people, heads and shoulders only. The person on the right is slightly in front of the person on the left. [`touchBarUserGroupTemplateName`](/documentation/appkit/nsimage/2646984-touchbarusergrouptemplatename)

 |  person.2.fill | Shows or represents information about a group of users. |

| The silhouette of a person’s head and shoulders. [`touchBarUserTemplateName`](/documentation/appkit/nsimage/2646949-touchbarusertemplatename)

 |  person.fill | Shows or represents information about a user. |

| A right-pointing speaker with one curved line on the right side, representing a sound wave. [`touchBarVolumeDownTemplateName`](/documentation/appkit/nsimage/2646928-touchbarvolumedowntemplatename)

 |  speaker.wave.1.fill | Decreases the volume. |

| A right-pointing speaker with two curved lines on the right side, representing sound waves. [`touchBarVolumeUpTemplateName`](/documentation/appkit/nsimage/2646987-touchbarvolumeuptemplatename)

 |  speaker.wave.3.fill | Increases the volume. |



### [Custom Touch Bar icons](/design/human-interface-guidelines/touch-bar#Custom-Touch-Bar-icons)

> ### [사용자 정의 터치 바 아이콘] (/디자인/인간-인터페이스-가이드라인/터치 바#사용자 정의 터치 바 아이콘)
>



If your app includes tasks or modes that can’t be represented by a system-provided Touch Bar image, you can create your own. [Apple Design Resources](https://developer.apple.com/design/resources/#macos-apps)

> 앱에 시스템에서 제공한 터치 바 이미지로 표현할 수 없는 작업이나 모드가 포함되어 있는 경우 자신만의 작업을 만들 수 있습니다. [애플 디자인 리소스] (https://developer.apple.com/design/resources/ #macos-apps)
>

 provides downloadable Photoshop and Sketch templates you can use to design properly scaled icons for the Touch Bar. For guidance, see [Icons](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/icons)

> 다운로드 가능한 Photoshop 및 스케치 템플릿을 제공합니다. 이 템플릿은 터치 바의 아이콘 크기를 적절히 조정하는 데 사용할 수 있습니다. 자세한 내용은 [Icons](https://developer.apple.com/design/human-interface-guidelines/design/human-interface-guidelines/icons) 를 참조하십시오
>

.



In general, create icons that look similar to the icons on the physical keyboard keys. Supply high-resolution images with a scale factor of @2x for all artwork that appears in the Touch Bar. To learn about image resolutions, see [Resolution](/design/human-interface-guidelines/images#Resolution)

> 일반적으로 실제 키보드 키의 아이콘과 유사한 모양의 아이콘을 만듭니다. 터치 바에 표시되는 모든 아트워크에 대해 축척 계수가 @2x인 고해상도 이미지를 제공합니다. 이미지 해상도에 대한 자세한 내용은 [해상도](/design/human-interface-가이드라인/images)를 참조하십시오#해상도)
>

.



**Design recognizable icons that clearly relate to your app on the main screen.** If necessary, you can vary the images to match the style of the Touch Bar.

> **기본 화면에서 앱과 명확하게 관련된 인식 가능한 아이콘을 디자인합니다.** 필요한 경우 터치 바의 스타일에 맞게 이미지를 변경할 수 있습니다.
>



**Avoid icons that extend to the full height of the Touch Bar.** In general, create icons that are no taller than 44 px (36 px for circular icons).

> **터치 바의 전체 높이까지 확장되는 아이콘은 피하십시오.** 일반적으로 44px(원형 아이콘의 경우 36px) 이하의 아이콘을 만듭니다.
>







|  |  |

| --- | --- |

| **Ideal icon size** | 18x18 pt (36x36 px @2x) |

| **Maximum icon size** | 22x22 pt (44x44 px @2x) |



![A row of six example icons, each of which has squares drawn around it, showing how it fits within areas that measure 36 pixels square and 44 pixels square.](https://docs-assets.developer.apple.com/published/d1bb25de8adb1ae4423d50695c8639bd/tb-custom-icon-example@2x.png)



**Keep icons optically centered.** Crop artwork to match the icon’s width, then add padding as needed to keep the icon optically centered when it’s displayed in a control.

> **아이콘을 광학 중심으로 유지합니다.** 아이콘의 너비와 일치하도록 아트워크를 잘라낸 다음 필요에 따라 패딩을 추가하여 아이콘이 컨트롤에 표시될 때 광학적으로 중앙에 있도록 합니다.
>



**Prefer a 45-degree angle for diagonal elements.** Using the same angle as in system icons like [`touchBarAudioInputMuteTemplateName`](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nsimage/2646941-touchbaraudioinputmutetemplatena)

> **대각 요소의 경우 45도 각도를 선호합니다.** ['touchBar]와 같은 시스템 아이콘과 동일한 각도 사용AudioInputMuteTemplateName'](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nsimage/2646941-touchbaraudioinputmutetemplatena)
>

 and [`touchBarComposeTemplateName`](/documentation/appkit/nsimage/2544716-touchbarcomposetemplatename)

 helps your custom icons look at home in the Touch Bar.

> 사용자 지정 아이콘이 터치 바에서 홈을 볼 수 있도록 도와줍니다.
>



**Avoid using color to communicate on and off states.** The system already changes the background appearance of standard controls that are in an off state.

> **색상을 사용하여 온/오프 상태로 통신하는 것을 피하십시오.** 시스템은 이미 오프 상태인 표준 컨트롤의 배경 모양을 변경합니다.
>



**Give most icons a 100% opacity fill.** To optimize readability, you might want to use a 70% opacity fill in combination with a 100% opacity fill. Use midtones only for improving readability and balance.

> **대부분의 아이콘에 불투명도를 100% 채웁니다.** 가독성을 최적화하려면 70% 불투명도 채우기를 100% 불투명도 채우기와 함께 사용할 수 있습니다. 가독성과 균형을 향상시키기 위해서만 중간음을 사용하십시오.
>



For guidance, see [Color](/design/human-interface-guidelines/touch-bar#Color)

.



**To match the style of the physical keyboard, give most icons a 2 px stroke.** If your design requires more visual weight, consider a 3 px stroke.

> ** 물리적 키보드의 스타일과 일치하려면 대부분의 아이콘을 2px 스트로크로 입력하십시오.** 설계에 더 많은 시각적 가중치가 필요한 경우 3px 스트로크를 고려하십시오.
>



**As much as possible, match the corner styles of the system images.** For example, use square corners for icons with a 2 px stroke, rounded corners with a 1px radius for icons with a 3 px stroke, and rounded corners with a 4 px radius for solid shapes.

> **시스템 이미지의 모서리 스타일을 최대한 일치시킵니다.** 예를 들어, 2px 스트로크가 있는 아이콘에는 정사각형 모서리를, 3px 스트로크가 있는 아이콘에는 1px 반경이 있는 둥근 모서리를, 솔리드 형상에는 4px 반경이 있는 둥근 모서리를 사용합니다.
>



[Controls and views](/design/human-interface-guidelines/touch-bar#Controls-and-views)

-------------------------------------------------------------------------------------



The system offers a range of standard controls you can provide in the app region of the Touch Bar. For consistency, use these controls when possible.

> 이 시스템은 터치 바의 앱 영역에서 제공할 수 있는 다양한 표준 컨트롤을 제공합니다. 일관성을 위해 가능한 한 이러한 컨트롤을 사용하십시오.
>



### [Buttons](/design/human-interface-guidelines/touch-bar#Buttons)



Buttons initiate app-specific actions, and can include an icon and a title.

> 버튼은 앱별 작업을 시작하며 아이콘과 제목을 포함할 수 있습니다.
>



![Partial screenshot of a Touch Bar in which a file button is highlighted.](https://docs-assets.developer.apple.com/published/32d43345c9a4e17d38ee7943034ddc2e/tb-cv-buttons@2x.png)



**Prefer icons over titles.** Strive to design clear icons that stand on their own without supporting text.

> **제목보다 아이콘을 선호합니다.** 텍스트를 지원하지 않고 스스로 서 있는 명확한 아이콘을 디자인하도록 노력합니다.
>



**Keep titles short.** Lengthy titles can crowd the Touch Bar.

> **제목을 짧게 유지합니다.** 긴 제목은 터치 바를 가득 채울 수 있습니다.
>



**Customize a button’s bezel color if necessary.** The system-provided button bezel looks similar to the physical keyboard buttons and contributes to a unified visual experience. If your app requires a custom bezel color, consider using a dark color, which tends to look good in the Touch Bar.

> **필요한 경우 버튼의 베젤 색상을 사용자 정의합니다.** 시스템 제공 버튼 베젤은 물리적인 키보드 버튼과 유사해 보이며 통합된 시각적 경험에 기여한다. 사용자 지정 베젤 색상이 필요한 경우 터치 바에서 잘 보이는 어두운 색상을 사용하는 것을 고려하십시오.
>



For guidance, see [Buttons](/design/human-interface-guidelines/buttons)

. For developer guidance, see [`NSButton`](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nsbutton)

> . 개발자 안내는 ['NS 버튼'](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nsbutton) 을 참조하십시오
>

.



#### [Toggles](/design/human-interface-guidelines/touch-bar#Toggles)



A toggle switches between on and off states.

> 토글은 온/오프 상태를 전환합니다.
>



![Partial screenshot of a Touch Bar that highlights a toggle button in the on state.](https://docs-assets.developer.apple.com/published/dcbcbf724fc6dde4d1d770f1ca1c193e/tb-cv-toggle-on@2x.png)On![Partial screenshot of a Touch Bar that highlights a toggle button in the off state.](https://docs-assets.developer.apple.com/published/7844cccb1e835013878e13ec21ad806a/tb-cv-toggle-off@2x.png)Off**Let the background indicate a toggle’s state.** The system automatically changes the background appearance of buttons in an off state, so there’s no need to indicate the state using color, text, or a different icon.



**Use toggles in place of checkboxes and radio buttons.** If you need a control that lets people choose between two states, use a toggle button.

> **확인란 및 라디오 버튼 대신 토글을 사용합니다.** 사람들이 두 상태 중 하나를 선택할 수 있는 컨트롤이 필요한 경우 전환 버튼을 사용하십시오.
>



For developer guidance, see the [`state`](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nsbutton/1528907-state)

> 개발자 안내는 ['state'](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nsbutton/1528907-state) 를 참조하십시오
>

 property of [`NSButton`](/documentation/appkit/nsbutton)

.



### [Candidate lists](/design/human-interface-guidelines/touch-bar#Candidate-lists)



A candidate list offers autocompletion suggestions during text entry. People can tap a suggestion to accept and insert it into the active text field or text view on the main screen. People can also expand or collapse a candidate list. An expanded candidate list replaces other controls that reside within the expansion area.

> 후보 목록은 텍스트 입력 중에 자동 완성 제안을 제공합니다. 사용자는 제안을 받아 들이고 메인 화면의 활성 텍스트 필드 또는 텍스트 보기에 삽입할 수 있습니다. 사람들은 후보 목록을 확장하거나 축소할 수도 있습니다. 확장된 후보 목록은 확장 영역 내에 있는 다른 컨트롤을 대체합니다.
>



![Screenshot of a Touch Bar that suggests the terms quick, quickly, and Quick in a candidate list.](https://docs-assets.developer.apple.com/published/e365ceb30b1f23779e99dc2c7b5b33d0/tb-cv-candidate-list@2x.png)



For developer guidance, see [`NSCandidateListTouchBarItem`](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nscandidatelisttouchbaritem)

> 개발자 지침은 [`NS 후보 목록]을 참조하십시오터치바 아이템'](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nscandidatelisttouchbaritem)
>

.



### [Character pickers](/design/human-interface-guidelines/touch-bar#Character-pickers)



A character picker opens a popover that includes a list of special characters, such as emoji. People can tap a character in the picker to insert it into the active text area on the main screen.

> 문자 선택기는 이모지와 같은 특수 문자 목록을 포함하는 팝업을 엽니다. 사용자는 선택기의 문자를 눌러 기본 화면의 활성 텍스트 영역에 삽입할 수 있습니다.
>



![Partial screenshot of a Touch Bar that highlights a character picker that’s collapsed.](https://docs-assets.developer.apple.com/published/a816d16db55cf4b0c6992f03078e4956/tb-cv-character-picker-collapsed@2x.png)Closed![Partial screenshot of a Touch Bar that highlights a character picker that’s expanded.](https://docs-assets.developer.apple.com/published/2685a55a41d329cecba7f53a1c771cf6/tb-cv-character-picker-expanded@2x.png)OpenFor developer guidance, see [`NSCandidateListTouchBarItem`](/documentation/appkit/nscandidatelisttouchbaritem)

.



### [Color pickers](/design/human-interface-guidelines/touch-bar#Color-pickers)



A color picker opens a popover that includes controls for selecting a color. You can configure a color picker to display an icon for a color picker, a stroke color picker, or a text color picker. Regardless of the icon, all color pickers display the same popover.

> 색상 선택기는 색상을 선택하는 컨트롤을 포함하는 팝업을 엽니다. 색상 선택기, 스트로크 색상 선택기 또는 텍스트 색상 선택기의 아이콘을 표시하도록 색상 선택기를 구성할 수 있습니다. 아이콘에 관계없이 모든 색상 선택기는 동일한 팝업을 표시합니다.
>



![Partial screenshot of a Touch Bar that highlights a color picker and a stroke color picker, both of which are collapsed.](https://docs-assets.developer.apple.com/published/42059c481e4c2402714340e81a08e104/tb-cv-color-picker-collapsed@2x.png)Closed![Screenshot of a Touch Bar that highlights a color picker that’s expanded.](https://docs-assets.developer.apple.com/published/1c5d20b6232122821f2bc7b2763084f5/tb-cv-color-picker-expanded@2x.png)Open**Use icons as intended.** Use the stroke color picker icon for selecting a stroke color. Use the text color picker icon for selecting a text color. For other color selection scenarios, use the color picker icon.



For developer guidance, see [`NSColorPickerTouchBarItem`](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nscolorpickertouchbaritem)

> 개발자 지침은 [`NScolorPicker]를 참조하십시오터치바 아이템'](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nscolorpickertouchbaritem)
>

.



### [Labels](/design/human-interface-guidelines/touch-bar#Labels)



A label displays read-only text that doesn’t appear within a control.

> 레이블은 컨트롤 내에 나타나지 않는 읽기 전용 텍스트를 표시합니다.
>



**In general, avoid labels.** Although the Touch Bar can display labels, it’s generally best to avoid them because they’re not interactive. Instead, focus on designing meaningful icons for your controls. If you must include a label, keep it as short as possible.

> **일반적으로 라벨을 사용하지 마십시오.** 터치 표시줄에 레이블을 표시할 수 있지만, 일반적으로 레이블은 대화식이 아니므로 레이블을 피하는 것이 가장 좋습니다. 대신 컨트롤에 대한 의미 있는 아이콘을 설계하는 데 집중하십시오. 라벨을 포함해야 하는 경우에는 가능한 한 짧게 유지하십시오.
>



**Prefer titles over labels when supplementing complex icons.** If the meaning of a control’s icon isn’t clear on its own, consider including a short title within the control to provide context.

> **복잡한 아이콘을 보완할 때 레이블보다 제목을 선호합니다.** 컨트롤 아이콘의 의미가 명확하지 않은 경우 컨트롤 내에 짧은 제목을 포함하여 컨텍스트를 제공하는 것을 고려하십시오.
>



![Partial screenshot of a Touch Bar in which two buttons are called out. One button displays a pin icon and uses the title \"Location.\" The other button displays a calendar icon and uses the title \"Time.\"](https://docs-assets.developer.apple.com/published/aaa0f4ad197ba971927a9938b6561901/tb-cv-buttons-with-titles@2x.png)



For guidance, see [Labels](/design/human-interface-guidelines/labels)

. For developer guidance, see [`NSTextField`](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nstextfield)

> . 개발자 안내는 ['NSTextField'](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nstextfield) 를 참조하십시오
>

.



### [Popovers](/design/human-interface-guidelines/touch-bar#Popovers)



A closed popover looks like a single button in the Touch Bar.

> 닫힌 팝업은 터치 바의 단일 버튼처럼 보입니다.
>



![Partial screenshot of a Touch Bar that highlights a closed popover for viewing items in columns.](https://docs-assets.developer.apple.com/published/e48964f9ee3e9b001f64cd250c3ecba4/tb-cv-popover-closed@2x.png)Closed![Screenshot of a Touch Bar that highlights an open popover that contains buttons for sorting options.](https://docs-assets.developer.apple.com/published/5d046fefb72e687e53c781df1d4342f7/tb-cv-popover-open@2x.png)OpenWhen it’s open, the popover replaces the current set of controls in the app region with a modal overlay containing a transient set of controls. In this modal overlay, people make a selection or tap a close button to return to the collapsed state and the previous set of controls.



Tip



In Touch Bar (2nd generation), the popover’s close button appears within the app region; in Touch Bar (1st generation), the close button replaces the system button. The second generation Touch Bar decreases the space available for popovers by 64 points and the system may display controls closer together to avoid clipping controls.

> 터치 바(2세대)에서는 팝업의 닫기 버튼이 앱 영역 내에 나타나고, 터치 바(1세대)에서는 닫기 버튼이 시스템 버튼을 대체합니다. 2세대 터치 바는 팝업에 사용할 수 있는 공간을 64점 줄이며, 시스템은 클립 컨트롤을 피하기 위해 컨트롤을 더 가까이에 표시할 수 있습니다.
>



Collapsed popovers open when people tap them. Optionally, popovers can also open in response to a touch and hold gesture. Popovers that support touch and hold include a trailing carat decoration.

> 무너진 포퍼는 사람들이 두드리면 열립니다. 선택적으로, 터치 앤 홀드 제스처에 응답하여 팝오버가 열릴 수도 있다. 터치 앤 홀드를 지원하는 팝오버에는 트레일링 캐럿 장식이 포함됩니다.
>



![Partial screenshot of a Touch Bar that highlights a closed popover for viewing items in columns.](https://docs-assets.developer.apple.com/published/314da988367c83ea201fc1eff922a5b7/tb-cv-collapsed-popover-closed@2x.png)Closed![Screenshot of a Touch Bar that highlights an open popover that contains buttons for sorting options.](https://docs-assets.developer.apple.com/published/f152dceafdacc50e16eed80f4c3a02a4/tb-cv-collapsed-popover-open@2x.png)OpenA popover can present the same overlay regardless of the gesture people use to expand it, or it can present a different overlay for each gesture. In a touch and hold overlay, people make a selection by sliding their holding finger to a control, and collapse the popover by lifting their finger.



**Use popovers sparingly.** Prefer Touch Bar controls that perform an action with a single tap.

> **팝오버는 조금만 사용하세요.** 한 번의 탭으로 작업을 수행하는 터치 바 컨트롤을 선호합니다.
>



**Avoid nesting popovers.** In general, don’t require people to navigate more than one level in the Touch Bar.

> **네스팅 팝업을 피하십시오.** 일반적으로 사용자가 터치 표시줄에서 두 개 이상의 레벨을 탐색할 필요가 없습니다.
>



**Reserve touch and hold for simple popovers.** Use touch and hold primarily to display an overlay that includes a simple set of options — such as a single segmented control — from which people can make a selection.

> **간단한 팝업을 위해 터치 앤 홀드를 예약하십시오.** 주로 터치 앤 홀드를 사용하여 사용자가 선택할 수 있는 단일 세그먼트 컨트롤과 같은 간단한 옵션 집합을 포함하는 오버레이를 표시합니다.
>



**Indicate choice selection in a collapsed popover.** When an expanded popover includes a list of options, show the currently selected option in the collapsed state.

> ** 축소된 팝업에서 선택 항목을 표시합니다.** 확장된 팝업에 옵션 목록이 포함된 경우 축소된 상태에서 현재 선택한 옵션을 표시합니다.
>



**Provide an obvious exit path.** Make sure people always know how to collapse a popover and return to the previous set of controls.

> **명확한 출구 경로를 제공합니다.** 팝업을 축소하고 이전 컨트롤로 돌아가는 방법을 사용자가 항상 알고 있는지 확인하십시오.
>



For developer guidance, see [`NSPopoverTouchBarItem`](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nspopovertouchbaritem)

For developer guidance, see [`NSPopoverTouchBarItem`](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nspopovertouchbaritem)

> 개발자 지침은 [`NSPopover]를 참조하십시오터치바 아이템'](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nspopovertouchbaritem)
>

.



### [Scrubbers](/design/human-interface-guidelines/touch-bar#Scrubbers)



A scrubber lets people swipe left and right to navigate through content like a list of dates or a group of photos. Scrubbers can be fixed or free, and are highly customizable — but need to retain an appearance that doesn’t feel out of place in the Touch Bar.

> 스크러버는 사람들이 왼쪽과 오른쪽으로 스와이프하여 날짜 목록이나 사진 그룹과 같은 내용을 탐색할 수 있도록 해줍니다. 스크러버는 고정 또는 무료로 사용할 수 있으며 사용자 정의가 매우 용이하지만 터치 바에서 어색하지 않은 외관을 유지해야 합니다.
>



For developer guidance, see [`NSScrubber`](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nsscrubber)

> 개발자 안내는 ['NSCruber'](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nsscrubber) 를 참조하십시오
>

.



#### [Fixed scrubbers](/design/human-interface-guidelines/touch-bar#Fixed-scrubbers)



A fixed scrubber allows for fluid, continuous interaction with a set of arranged content, such as open Safari tabs. As people swipe across the scrubber, items beneath their finger become highlighted. Depending on the scrubber’s configuration, people make a selection by moving a finger to the item, or by lifting their finger from the scrubber. If the amount of content exceeds the size of a fixed scrubber, the scrubber automatically scrolls to reveal additional items as the finger nears the edge of the control. In a fixed scrubber, people use a finger to move the selection, rather than the content.

> 고정 스크러버를 사용하면 열려 있는 Safari 탭과 같이 배열된 컨텐츠 집합과 유동적이고 지속적으로 상호 작용할 수 있습니다. 사람들이 수세미를 가로질러 미끄러지면서 손가락 밑에 있는 물건들이 강조됩니다. 스크러버의 구성에 따라 사람들은 항목으로 손가락을 움직이거나 스크러버에서 손가락을 들어 올려 선택합니다. 콘텐츠의 양이 고정된 스크러버의 크기를 초과하면 손가락이 컨트롤의 가장자리에 가까워지면 스크러버가 자동으로 스크롤하여 추가 항목을 표시합니다. 고정된 스크러버에서 사람들은 콘텐츠가 아닌 손가락을 사용하여 선택 영역을 이동합니다.
>



![Screenshot of a Touch Bar that highlights a fixed scrubber. The six items in the scrubber are six different Safari pages. The third item from the left is selected.](https://docs-assets.developer.apple.com/published/9e67256da4a516b4031cb59583aa376a/tb-cv-fixed-scrubber@2x.png)



#### [Free scrubbers](/design/human-interface-guidelines/touch-bar#Free-scrubbers)



A free scrubber presents content in a scrollable list — such as a list of Calendar dates — that people swipe to scroll. Depending on the scrubber’s configuration, people select an item by moving it to a specific location, like the center of the scrubber, or by tapping the item while the scrubber is stationary.

> 무료 스크러버는 일정관리 날짜 목록과 같은 스크롤 가능한 목록에 사용자가 스크롤하기 위해 스와이프하는 내용을 표시합니다. 스크러버의 구성에 따라 사람들은 스크러버의 중앙과 같은 특정 위치로 항목을 이동하거나 스크러버가 정지된 상태에서 항목을 탭하여 항목을 선택합니다.
>



**Use predictable and logically ordered values.** When the scrollable list in a free scrubber is stationary, some values may be hidden. If the list displays items in a logical order that follows an obvious progression, people can predict the hidden values and move through the list quickly. When viewing a list of country or region names, for example, people are generally better at predicting hidden values in an alphabetized list than in a list ordered by population size.

> **예측 가능하고 논리적으로 순서가 지정된 값을 사용합니다.** 자유 스크러버에서 스크롤 가능한 목록이 고정되어 있으면 일부 값이 숨겨질 수 있습니다. 목록이 명확한 진행률을 따르는 논리적 순서로 항목을 표시하면, 사람들은 숨겨진 값을 예측하고 목록을 빠르게 이동할 수 있다. 예를 들어, 국가 또는 지역 이름 목록을 볼 때, 사람들은 일반적으로 인구 크기에 따라 순서가 정해진 목록보다 알파벳순으로 정렬된 목록에서 숨겨진 값을 더 잘 예측한다.
>



**Keep lists of values as short as possible.** People can find it tedious to navigate long lists in the Touch Bar. If you have a large list of values, consider presenting it on the main screen instead of the Touch Bar, so people can use the keyboard or trackpad for navigation.

> **값 목록을 최대한 짧게 유지하십시오.** 사람들은 터치 바에서 긴 목록을 탐색하는 것이 지루하다고 느낄 수 있다. 값 목록이 많은 경우 키보드 또는 트랙패드를 탐색에 사용할 수 있도록 터치 바 대신 주 화면에 표시하는 것을 고려해 보십시오.
>



### [Segmented controls](/design/human-interface-guidelines/touch-bar#Segmented-controls)



A segmented control is a linear set of two or more segments, each of which functions as a button — usually configured as a toggle. Within the control, all segments are equal in width. Like buttons, segments can contain text and icons.

> 세그먼트 컨트롤은 두 개 이상의 세그먼트로 구성된 선형 세트이며, 각 세그먼트는 버튼으로 기능합니다(일반적으로 토글로 구성됩니다). 컨트롤 내에서 모든 세그먼트의 너비는 동일합니다. 버튼과 마찬가지로 세그먼트에는 텍스트와 아이콘이 포함될 수 있습니다.
>



![Partial screenshot of a Touch Bar that highlights a text justification segmented control that contains four segments.](https://docs-assets.developer.apple.com/published/f152dceafdacc50e16eed80f4c3a02a4/tb-cv-segmented-controls@2x.png)



**Limit the number of segments to improve usability.** Wider segments are easier for people to tap.

> **사용성을 향상시키기 위해 세그먼트 수를 제한합니다.** 더 넓은 부분은 사람들이 탭하기에 더 쉽다.
>



**Prefer icons over titles.** Strive to design clear icons that stand on their own without requiring supporting text.

> **제목보다 아이콘을 선호합니다.** 지원 텍스트 없이 스스로 서 있는 명확한 아이콘을 디자인하기 위해 노력합니다.
>



**Try to keep segment content size consistent.** Because segments match in width, it’s visually coherent if the content in the segments is also equal in length.

> **세그먼트 콘텐츠 크기를 일관되게 유지하도록 노력하십시오.** 세그먼트는 너비가 일치하므로 세그먼트의 내용도 길이가 같으면 시각적으로 일관성이 있습니다.
>



**Keep titles short.** Lengthy titles can crowd the Touch Bar.

> **제목을 짧게 유지합니다.** 긴 제목은 터치 바를 가득 채울 수 있습니다.
>



**Prefer darker colors for bezel color changes.** The appearance of the system-provided bezel resembles physical keyboard buttons. If your app requires a custom bezel color, dark colors are recommended.

> ** 베젤 색상 변경은 어두운 색상을 선호합니다.** 시스템이 제공하는 베젤의 외관은 물리적인 키보드 버튼과 유사하다. 앱에 사용자 지정 베젤 색상이 필요한 경우 어두운 색상이 권장됩니다.
>



For developer guidance, see [`NSSegmentedControl`](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nssegmentedcontrol)

> 개발자 지침은 ['NS Segmented Control'](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nssegmentedcontrol) 을 참조하십시오
>

.



### [Sharing service pickers](/design/human-interface-guidelines/touch-bar#Sharing-service-pickers)



People use sharing service pickers to share text, images, and other content with apps, social media accounts, and other services. When people tap a sharing service picker, it displays a popover that contains sharing buttons.

> 사람들은 공유 서비스 피커를 사용하여 텍스트, 이미지 및 기타 콘텐츠를 앱, 소셜 미디어 계정 및 기타 서비스와 공유합니다. 사용자가 공유 서비스 선택기를 누르면 공유 버튼이 포함된 팝업이 표시됩니다.
>



![Partial screenshot of a Touch Bar that highlights a sharing service picker in a closed state.](https://docs-assets.developer.apple.com/published/fad03c9101cc3c16641e836ed124c2e4/tb-cv-sharing-picker-closed@2x.png)Closed![Partial screenshot of a Touch Bar that highlights a sharing service picker in an open state.](https://docs-assets.developer.apple.com/published/99591462b4f3eab1a579c96dc53b5b3d/tb-cv-sharing-picker-open@2x.png)Open**Present a sharing service picker only when there’s content to share.** If people haven’t selected text, images, or other sharable content, the sharing service picker needs to be unavailable.



For developer guidance, see [`NSSharingServicePicker`](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nssharingservicepicker)

> 개발자 안내는 ['NS 공유 서비스 피커'](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nssharingservicepicker) 를 참조하십시오
>

.



### [Sliders](/design/human-interface-guidelines/touch-bar#Sliders)



A slider is a horizontal track with a control called a thumb, which people can slide to move between a minimum and maximum value, such as screen brightness level, or position during media playback. As a slider’s value changes, the portion of track between the minimum value and the thumb fills with color.

> 슬라이더는 엄지손가락이라는 컨트롤이 있는 수평 트랙으로, 사람들이 화면 밝기 수준이나 미디어 재생 중 위치와 같은 최소와 최대 값 사이를 이동하도록 슬라이드할 수 있습니다. 슬라이더의 값이 변경되면 최소 값과 엄지 사이의 트랙 부분이 색상으로 채워집니다.
>



![Partial screenshot of a Touch Bar that highlights a sharing service picker in an open state.](https://docs-assets.developer.apple.com/published/82d9de0501fa09107e4bab1c528f1ea1/tb-cv-slider@2x.png)



**Customize a slider’s appearance to match your app and add value.** Consider coordinating a slider’s track color with your app’s color scheme.

> **슬라이더 모양을 앱에 맞게 사용자 지정하고 가치를 추가합니다.** 슬라이더의 트랙 색상을 앱의 색상 체계와 조정하는 것을 고려해 보십시오.
>



**Consider using a stepper instead of a slider when space is tight.** If a slider’s values cover a limited range and it’s possible to move through them in discrete steps, it might make sense to use a stepper. For guidance, see [Steppers](/design/human-interface-guidelines/touch-bar#Steppers)

> **공간이 좁을 때 슬라이더 대신 스테퍼를 사용하는 것을 고려해보세요.** 슬라이더의 값이 제한된 범위를 포함하고 개별 단계로 슬라이더를 이동할 수 있다면 스테퍼를 사용하는 것이 합리적일 수 있습니다. 자세한 지침은 [Stepers](/design/human-interface-guideline/touch-bar#Stepers)를 참조하십시오
>

.



**Provide left and right icons that illustrate the meaning of the minimum and maximum values.** A slider that adjusts image size, for example, could show a small image icon on the left and a large image icon on the right.

> **최소값과 최대값의 의미를 나타내는 왼쪽 및 오른쪽 아이콘을 제공합니다.** 예를 들어, 이미지 크기를 조정하는 슬라이더는 왼쪽에 작은 이미지 아이콘을 표시하고 오른쪽에 큰 이미지 아이콘을 표시할 수 있습니다.
>



For developer guidance, see [`NSSlider`](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nsslider)

> 개발자 안내는 ['NS슬라이더'](https://developer.apple.com/design/human-interface-guidelines/documentation/appkit/nsslider) 를 참조하십시오
>

.



### [Steppers](/design/human-interface-guidelines/touch-bar#Steppers)



Steppers provide a set of continuous — usually numeric — values from which people can choose. A stepper displays the current value centered between a decrementing control and an incrementing control. People tap the controls or swipe the current value left or right to change the value by an amount you specify.

> 스텝퍼는 사람들이 선택할 수 있는 연속형(일반적으로 숫자) 값 집합을 제공합니다. 스텝퍼는 감소하는 컨트롤과 증가하는 컨트롤 사이에 중심이 되는 현재 값을 표시합니다. 사람들은 사용자가 지정한 양만큼 값을 변경하기 위해 컨트롤을 누르거나 현재 값을 왼쪽 또는 오른쪽으로 스와이프합니다.
>



![Partial screenshot of a Touch Bar that highlights a font-size stepper with a current value of 22 points.](https://docs-assets.developer.apple.com/published/9565a3385c551a7aa1d077d738146cc6/tb-cv-steppers@2x.png)



**Display the item’s current value in the center view.** By default, a stepper uses text to display the current value. You can use a formatter to style the text — for example, in a stepper that lets people choose dates, you might make today’s date red. In some cases, it might make sense to use images instead of text, but it can be tricky to create images that convey a logical progression from which people can predict the values that precede and follow the current value. For example, a stepper that controls the line weight of a marking tool could use a set of images that vary in thickness to help people understand the effect of incrementing and decrementing the value.

> **중앙 보기에 항목의 현재 값을 표시합니다.** 기본적으로 스테퍼는 텍스트를 사용하여 현재 값을 표시합니다. 형식을 사용하여 텍스트 스타일을 지정할 수 있습니다. 예를 들어 사용자가 날짜를 선택할 수 있는 단계에서 오늘 날짜를 빨간색으로 만들 수 있습니다. 경우에 따라 텍스트 대신 이미지를 사용하는 것이 합리적일 수 있지만, 사람들이 현재 가치에 선행하고 따르는 가치를 예측할 수 있는 논리적인 진행을 전달하는 이미지를 만드는 것은 어려울 수 있다. 예를 들어, 마킹 도구의 선 무게를 제어하는 스테퍼는 사람들이 값의 증가와 감소의 효과를 이해하도록 돕기 위해 두께가 다른 이미지 세트를 사용할 수 있다.
>



**Avoid using a stepper when people are likely to make large adjustments to an item’s value.** Because a stepper changes an item’s value by one discrete step per swipe or tap, people would have to swipe or tap a lot to make a large value change.

> ** 사람들이 물건의 가치를 크게 조정할 가능성이 있는 경우에는 스테퍼를 사용하지 마십시오.** 스텝퍼는 물건의 값을 스와이프 또는 탭 당 한 번의 개별 단계로 변경하기 때문에, 큰 값 변경을 위해 사람들은 스와이프 또는 탭을 많이 해야 할 것이다.
>



[Platform considerations](/design/human-interface-guidelines/touch-bar#Platform-considerations)

-----------------------------------------------------------------------------------------------



*Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.*

> *iOS, iPadOS, tvOS, 비전에서 지원되지 않음OS 또는 시계OS.*
>



[Resources](/design/human-interface-guidelines/touch-bar#Resources)

-------------------------------------------------------------------



#### [Related](/design/human-interface-guidelines/touch-bar#Related)



[Feedback](/design/human-interface-guidelines/feedback)





#### [Developer documentation](/design/human-interface-guidelines/touch-bar#Developer-documentation)



[`NSTouchBar`](/documentation/appkit/nstouchbar)





