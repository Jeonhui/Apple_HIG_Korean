# **[technologies] wallet**

# Wallet helps people securely store their credit and debit cards, driver’s license or state ID, transit cards, event tickets, keys, and more on iPhone and Apple Watch.
> 지갑은 사람들이 신용카드와 직불카드, 운전면허증이나 신분증, 교통카드, 이벤트 티켓, 열쇠 등을 아이폰과 애플워치에 안전하게 저장할 수 있도록 도와준다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Wallet-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Wallet-intro_2x.png)

People use their cards and passes in Wallet to make Apple Pay — and Apple Pay Later — purchases, track their orders, confirm their identity, and streamline activities like boarding a plane, attending a concert, or receiving a discount.
> 사람들은 애플 페이(Apple Pay)와 애플 페이 라이터(Apple Pay Later)를 구매하고, 주문을 추적하고, 신원을 확인하며, 비행기 탑승, 콘서트 참석 또는 할인과 같은 활동을 간소화하기 위해 자신의 카드와 패스를 사용합니다.
>




When you integrate Apple Wallet into your app, you can create custom passes and present them the moment people need them, securely verify an individual’s identity so they can access personal content, and offer detailed receipts and tracking information where it’s most convenient. For developer guidance, see [Wallet](https://developer.apple.com/documentation/passkit/wallet).
> Apple Wallet을 앱에 통합하면 사용자 지정 패스를 생성하여 필요한 순간에 제시하고, 개인 컨텐츠에 액세스할 수 있도록 개인의 신원을 안전하게 확인하고, 가장 편리한 곳에서 상세한 영수증 및 추적 정보를 제공할 수 있습니다. 개발자 지침은 지갑을 참조하십시오.
>




# **Passes**

**Offer to add new passes to Wallet.** When people do something that results in a new pass — like checking into a flight, purchasing an event ticket, or registering for a store reward program — you can present system-provided UI that helps them add the pass to Wallet with one tap (for developer guidance, see [addPasses(_:withCompletionHandler:)](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617093-addpasses)). If people want to review a pass before adding it, you can display a custom view that displays the pass and provides an Add to Apple Wallet button; for developer guidance, see [PKAddPassesViewController](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller).
> 사람들이 비행기 탑승 수속, 이벤트 티켓 구입, 상점 보상 프로그램 등록 등 새로운 패스를 할 때 한 번의 탭으로 월렛에 패스를 추가할 수 있는 시스템 제공 UI를 제시할 수 있습니다(개발자 지침은 패스 추가(_:CompletionHandler:)). 사용자가 패스를 추가하기 전에 확인하려는 경우 패스를 표시하고 Apple Wallet에 추가 단추를 제공하는 사용자 정의 뷰를 표시할 수 있습니다. 개발자 지침은 PKAddPassesViewController를 참조하십시오.
>




**Help people add a pass that they created outside of your app.** If people create a pass using your website or another device, suggest adding it to Wallet the next time they open your app. If people decline your suggestion, don’t ask them again.
> 다른 사람들이 당신의 앱 밖에서 만든 패스를 추가할 수 있도록 도와줍니다. 만약 사람들이 당신의 웹사이트나 다른 기기를 사용하여 패스를 만든다면, 그들이 다음에 당신의 앱을 열 때 지갑에 그것을 추가할 것을 제안합니다. 만약 사람들이 당신의 제안을 거절한다면, 그들에게 다시 묻지 마세요.
>




**Add related passes as a group.** If your app generates multiple passes, like boarding passes for a multi-connection flight, add all passes at the same time so people don’t have to add each one individually. If people can receive a group of passes from your website — such as a set of tickets for an event — bundle them together so that people can download all of them at one time. For developer guidance, see [Distributing and updating a pass](https://developer.apple.com/documentation/walletpasses/distributing_and_updating_a_pass).
> 단체로 관련 패스를 추가합니다. 다중 연결 항공편의 탑승권과 같이 앱에서 여러 개의 패스를 생성하는 경우, 사람들이 개별적으로 추가할 필요가 없도록 모든 패스를 동시에 추가하십시오. 이벤트 티켓 세트와 같은 사용자가 웹 사이트에서 패스 그룹을 받을 수 있는 경우 한 번에 모든 패스를 다운로드할 수 있도록 패스 그룹을 함께 묶습니다. 개발자 지침은 패스 배포 및 업데이트를 참조하십시오.
>




**Display an Add to Apple Wallet button to let people add an existing pass that isn’t already in Wallet.** If people previously declined your suggestion to add a pass to Wallet — or if they removed the pass — a button makes it easy to add it if they change their minds. You can display an Add to Apple Wallet button wherever the corresponding pass information appears in your app. For developer guidance, see [PKAddPassButton](https://developer.apple.com/documentation/passkit/pkaddpassbutton). You can also display an Add to Apple Wallet badge in an email or on a webpage; for guidance, see [Add to Apple Wallet guidelines](https://developer.apple.com/wallet/add-to-apple-wallet-guidelines/).
> 아직 지갑에 없는 기존 패스를 추가할 수 있도록 하려면 Apple Wallet에 추가 단추를 표시합니다. 이전에 다른 사람이 지갑에 패스를 추가하라는 사용자의 제안을 거부했거나 패스를 제거한 경우 단추를 누르면 마음이 바뀌어도 쉽게 추가할 수 있습니다. Apple Wallet에 추가 버튼은 해당 패스 정보가 앱에 표시되는 곳마다 표시할 수 있습니다. 개발자 지침은 PKAddPassButton을 참조하십시오. 전자 메일이나 웹 페이지에 Apple Wallet에 추가 배지를 표시할 수도 있습니다. 자세한 내용은 Apple Wallet에 추가 지침을 참조하십시오.
>




**Let people jump from your app to their pass in Wallet.** Wherever your app displays information about a pass that exists in Wallet, you can offer a link that opens it directly. Label the link something like “View in Wallet.”
> 사람들이 당신의 앱에서 지갑의 그들의 패스로 점프할 수 있게 해주세요. 당신의 앱이 지갑에 존재하는 패스에 대한 정보를 표시하는 곳이라면, 당신은 그것을 직접 여는 링크를 제공할 수 있습니다. 링크에 "지갑에서 보기"와 같은 레이블을 지정합니다
>




**Consider hiding expired passes.** In iOS 15 and later, Wallet automatically hides expired passes to reduce crowding, while also providing a button that lets people revisit them. To ensure the system hides passes appropriately, set the expiration date, relevant date, and voided properties of each pass correctly; for developer guidance, see [Pass](https://developer.apple.com/documentation/walletpasses/pass/).
> 만료된 패스를 숨기는 것을 고려해보세요. iOS 15 이상에서는 Wallet이 만료된 패스를 자동으로 숨겨서 혼잡을 줄이는 동시에 다시 방문할 수 있는 버튼을 제공합니다. 시스템이 패스를 적절하게 숨기려면 각 패스의 만료 날짜, 관련 날짜 및 무효 속성을 올바르게 설정하십시오. 개발자 지침은 패스를 참조하십시오.
>




**Always get people’s permission before deleting a pass from Wallet.** For example, you could include an in-app setting that lets people specify whether they want to delete passes manually or have them removed automatically. If necessary, you can display an alert before deleting a pass.
> 수동으로 패스를 삭제할지 또는 자동으로 삭제할지 여부를 지정할 수 있는 앱 내 설정을 포함할 수 있습니다. 필요한 경우 패스를 삭제하기 전에 경고를 표시할 수 있습니다.
>




**Help the system suggest a pass on the Lock Screen when it’s contextually relevant.** Ideally, passes automatically appear when they’re needed so people don’t have to manually locate them. When you supply information about when and where your pass is relevant, the system can display a link to it on the Lock Screen when people are most likely to want it. For example, a gym membership card could appear on the Lock Screen as people enter the gym. For developer guidance, see [Showing a pass on the Lock Screen](https://developer.apple.com/documentation/walletpasses/pass/showing_a_pass_on_the_lock_screen/).
> 시스템에서 잠금 화면에 대한 패스를 제안할 수 있도록 도와줍니다. 패스가 필요할 때 자동으로 나타나므로 수동으로 패스를 찾을 필요가 없습니다. 언제 어디서 패스와 관련된 정보를 제공하면, 사람들이 가장 원할 때 시스템이 해당 패스에 대한 링크를 잠금 화면에 표시할 수 있습니다. 예를 들어, 사람들이 체육관에 들어갈 때 체육관 회원 카드가 잠금 화면에 나타날 수 있습니다. 개발자 지침은 잠금 화면에 패스 표시를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/screen-notification_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/screen-notification_2x.png)

**Update passes as needed.** Physical passes don’t typically change, but a digital pass should reflect updates to events. An airline boarding pass, for example, should automatically update to display flight delays and gate changes.
> 물리적 패스는 일반적으로 변경되지 않지만 디지털 패스는 이벤트에 대한 업데이트를 반영합니다. 예를 들어, 항공사 탑승권은 자동으로 비행 지연과 게이트 변경을 표시하도록 업데이트되어야 한다.
>




**Use change messages only for updates to time-critical information.** A change message interrupts the user’s current workflow, so it’s essential to send one only when you make an update that people must know about. For example, people need to know when there’s a gate change in a boarding pass, but they don’t need to know when a customer service phone number changes. Never use a change message for marketing or other noncritical communication. You enable change messages on a per-field basis; for developer guidance, see [Adding a web service to update passes](https://developer.apple.com/documentation/walletpasses/adding_a_web_service_to_update_passes/).
> 변경 메시지는 시간이 중요한 정보에 대한 업데이트에만 사용하십시오. 변경 메시지는 사용자의 현재 워크플로우를 중단하므로 사용자가 알아야 할 업데이트를 할 때만 메시지를 전송해야 합니다. 예를 들어 탑승권에 게이트 변경이 있을 때는 알아야 하지만 고객 서비스 전화번호가 변경될 때는 알 필요가 없습니다. 마케팅이나 기타 중요하지 않은 커뮤니케이션을 위해 변경 메시지를 사용하지 마십시오. 필드별로 변경 메시지를 사용할 수 있습니다. 개발자 지침은 업데이트 패스에 웹 서비스 추가를 참조하십시오.
>




# **Designing passes**

Wallet uses a consistent design aesthetic to strengthen familiarity and build trust. Instead of merely replicating the appearance of a physical item, design a clean, simple pass that looks at home in Wallet.
> 지갑은 일관된 디자인 미학을 사용하여 친숙함을 강화하고 신뢰를 쌓는다. 단순히 실제 항목의 모양을 복제하는 대신 지갑에서 집을 볼 수 있는 깨끗하고 간단한 패스를 설계하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/pass-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/pass-intro_2x.png)

**Design a pass that looks great and works well on all devices.** Passes can look different on different devices. For example, when a pass appears on Apple Watch, it doesn’t display all the images it displays when it appears on iPhone (for guidance, see [Passes for Apple Watch](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#passes-for-apple-watch)). Don’t put essential information in elements that might be unavailable on certain devices. Also, don’t add padding to images; for example, watchOS crops white space from some images.
> 보기 좋고 모든 장치에서 잘 작동하는 패스를 설계하십시오. 패스는 장치마다 다르게 보일 수 있습니다. 예를 들어 Apple Watch에 패스가 표시될 때 iPhone에 표시되는 모든 이미지가 표시되지는 않습니다(자세한 내용은 Apple Watch용 패스 참조). 특정 장치에서 사용할 수 없는 요소에는 필수 정보를 넣지 마십시오. 또한 이미지에 패딩을 추가하지 마십시오(예: 보기)OS는 일부 이미지에서 빈 공간을 잘라냅니다.
>




**Avoid using device-specific language.** You can’t predict the device people will use to view your pass, so don’t include copy that might not make sense on a particular device. For example, copy that tells people to “slide to view” content doesn’t make sense when it appears on Apple Watch.
> 장치별 언어를 사용하지 마십시오. 사람들이 사용자의 패스를 볼 때 사용할 장치를 예측할 수 없으므로 특정 장치에서 의미가 없는 복사본을 포함하지 마십시오. 예를 들어, 사람들에게 내용을 "보기 위해 슬라이드"하라고 말하는 복사본은 Apple Watch에 표시될 때 의미가 없습니다.
>




**Make your pass instantly identifiable.** Using color — especially a color that’s linked to your brand — can help people recognize your pass as soon as they see it. Make sure that pass content remains comfortably readable against the background you choose.
> 색상(특히 브랜드와 연결된 색상)을 사용하면 사람들이 사용자의 패스를 보자마자 인식할 수 있습니다. 통과 내용이 선택한 배경에서 편안하게 읽을 수 있는지 확인합니다.
>




**Keep the front of a pass uncluttered so people can get important information at a glance.**Show essential information — like an event date or account balance — in the top-right area of the pass so people can still see it when the pass is collapsed in Wallet. Use the rest of the pass front to provide important information; consider putting extra information on the back of a pass (iOS) or in a details screen (watchOS).
> 사람들이 한 눈에 중요한 정보를 얻을 수 있도록 통행증 앞을 어질러 놓지 마세요.이벤트 날짜 또는 계정 잔액과 같은 필수 정보를 패스의 오른쪽 상단 영역에 표시하여 패스가 Wallet에서 축소되어도 계속 볼 수 있도록 합니다. 중요한 정보를 제공하려면 패스 프론트의 나머지 부분을 사용하십시오. 패스 뒷면(iOS) 또는 상세 화면(워치OS)에 추가 정보를 넣는 것을 고려하십시오.
>




**Prefer an NFC-enabled pass.** People appreciate having a contactless pass, because it means that they can just hold their device near a reader. If you support both NFC and a barcode or QR code, the code appears on the back of the pass (in iOS) or in the details screen (in watchOS). In iOS, you can display a QR code or barcode on the front of your pass if necessary for your design.
> 근거리 무선 통신이 가능한 패스를 선호한다. 사람들은 비접촉식 패스를 갖는 것을 좋아한다. 왜냐하면 그것은 그들이 그들의 기기를 리더기 근처에 둘 수 있다는 것을 의미하기 때문이다. NFC와 바코드 또는 QR 코드를 모두 지원하는 경우, 코드는 패스 뒷면(iOS)이나 세부 정보 화면(watchOS)에 나타납니다. iOS에서는 디자인에 필요한 경우 QR 코드나 바코드를 패스 앞면에 표시할 수 있습니다.
>




**Reduce image sizes for optimal performance.** People can receive passes via email or a webpage. To make downloads as fast as possible, use the smallest image files that still look great.
> 최적의 성능을 위해 이미지 크기를 줄입니다. 사람들은 이메일이나 웹페이지를 통해 패스를 받을 수 있습니다. 가능한 한 빨리 다운로드하려면 보기 좋은 최소 이미지 파일을 사용하십시오.
>




**Provide an icon that represents your company or brand.** The system includes your icon when displaying information about a relevant pass on the lock screen. Mail also uses the icon to represent your pass in an email message. You can use your app icon or design an icon for this purpose. Create an icon that measures a minimum of 38x38 pts.
> 회사 또는 브랜드를 나타내는 아이콘을 제공하십시오. 시스템은 잠금 화면에 관련 패스에 대한 정보를 표시할 때 아이콘을 포함합니다. 메일은 또한 전자 메일 메시지에서 사용자의 암호를 나타내기 위해 아이콘을 사용합니다. 이를 위해 앱 아이콘을 사용하거나 아이콘을 디자인할 수 있습니다. 최소 38x38ppt을 측정하는 아이콘을 만듭니다.
>




The system defines several pass *styles*, each of which specifies the overall appearance of a pass in categories like event ticket, boarding pass, and coupon. The pass style determines the layout of your content, and can affect the types of relevancy information you provide (for guidance, see [Passes](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#passes)).
> 시스템은 이벤트 티켓, 탑승권 및 쿠폰과 같은 범주에서 패스의 전체적인 모양을 지정하는 여러 개의 패스 스타일을 정의합니다. 통과 유형은 내용의 레이아웃을 결정하며, 제공하는 관련 정보 유형에 영향을 미칠 수 있습니다(참고 사항은 통과 참조).
>




Although each pass style is different, all styles display information using the basic layout areas shown below:
> 각 통과 스타일은 다르지만, 모든 스타일은 아래에 표시된 기본 레이아웃 영역을 사용하여 정보를 표시합니다:
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/pass-layout-diagram_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/pass-layout-diagram_2x.png)

All passes display a logo image; depending on style, passes can display additional images in other areas. To display text, you use the following [pass fields](https://developer.apple.com/documentation/walletpasses/passfields) to provide content within specific layout areas:
> 모든 패스는 로고 이미지를 표시합니다. 스타일에 따라 패스는 다른 영역에 추가 이미지를 표시할 수 있습니다. 텍스트를 표시하려면 다음 암호 필드를 사용하여 특정 레이아웃 영역 내에서 내용을 제공합니다:
>




| Field | Layout area | Use to provide... |
| --- | --- | --- |
| Header | Essential | Critical information that should remain visible when the pass is collapsed in Wallet. |
| Primary | Primary | Important information that helps people use the pass. |
| Secondary and auxiliary | Secondary and auxiliary | Useful information that people might not need every time they use the pass. |
| Back | Not shown in diagram | Supplemental details that don’t need to be on the pass front. |

In general, a pass can have up to three header fields, one primary field, up to four secondary fields, and up to four auxiliary fields. Depending on the amount of content you display in each field, some fields may not be visible.
> 일반적으로 패스는 최대 3개의 헤더 필드, 1개의 기본 필드, 4개의 보조 필드 및 4개의 보조 필드를 가질 수 있습니다. 각 필드에 표시하는 내용의 양에 따라 일부 필드가 표시되지 않을 수 있습니다.
>




**Display text only in pass fields.** The system ensures that text in pass fields is legible and accessible to assistive technologies like VoiceOver. Don’t embed text in images — it’s not accessible and not all images are displayed on all devices — and avoid using custom fonts that might make text hard to read.
> 암호 필드에만 텍스트를 표시합니다. 이 시스템은 암호 필드의 텍스트를 읽을 수 있고 VoiceOver와 같은 보조 기술에 액세스할 수 있도록 보장합니다. 이미지에 텍스트를 포함하지 마십시오. 액세스할 수 없고 일부 이미지가 모든 장치에 표시되지 않습니다. 또한 텍스트를 읽기 어렵게 만들 수 있는 사용자 지정 글꼴을 사용하지 마십시오.
>




# **Boarding passes**

Use the boarding pass style for train tickets, airline boarding passes, and other types of transit passes. Typically, each pass corresponds to a single trip with a specific starting and ending point.
> 기차표, 항공사 탑승권 및 기타 유형의 환승권에는 탑승권 스타일을 사용합니다. 일반적으로 각 패스는 특정 시작점과 종료점이 있는 단일 트립에 해당합니다.
>




A boarding pass can display logo and footer images, and it can have up to two primary fields and up to five auxiliary fields.
> 탑승권은 로고 및 바닥글 이미지를 표시할 수 있으며, 최대 2개의 기본 필드와 최대 5개의 보조 필드를 가질 수 있습니다.
>




• [Example](../technologies/wallet#)
• [Layout](../technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/boarding_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/boarding_2x.png)


# **Coupons**

Use the coupon style for coupons, special offers, and other discounts. A coupon can display logo and strip images, and it can have up to four secondary and auxiliary fields, all displayed on one row.
> 쿠폰, 특별 할인 및 기타 할인에 쿠폰 스타일을 사용합니다. 쿠폰은 로고와 스트립 이미지를 표시할 수 있으며, 한 행에 표시되는 보조 및 보조 필드를 최대 4개까지 포함할 수 있습니다.
>




• [Example](../technologies/wallet#)
• [Layout](../technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/coupon_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/coupon_2x.png)


# **Store cards**

Use the store card style for store loyalty cards, discount cards, points cards, and gift cards. If an account related to a store card carries a balance, the pass usually shows the current balance.
> 상점 충성도 카드, 할인 카드, 포인트 카드 및 기프트 카드에 상점 카드 스타일을 사용합니다. 매장 카드와 관련된 계좌에 잔액이 있을 경우, 패스는 보통 현재 잔액을 보여준다.
>




A store card can display logo and strip images, and it can have up to four secondary and auxiliary fields, all displayed on one row.
> 상점 카드는 로고 및 스트립 이미지를 표시할 수 있으며 최대 4개의 보조 및 보조 필드를 가질 수 있으며, 모두 한 행에 표시됩니다.
>




• [Example](../technologies/wallet#)
• [Layout](../technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/store-card_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/store-card_2x.png)


# **Event tickets**

Use the event ticket style to give people entry into events like concerts, movies, plays, and sporting events. Typically, each pass corresponds to a specific event, but you can also use a single pass for several events, as with a season ticket.
> 이벤트 티켓 스타일을 사용하여 사람들에게 콘서트, 영화, 연극 및 스포츠 이벤트와 같은 이벤트에 입장할 수 있습니다. 일반적으로 각 패스는 특정 이벤트에 해당하지만 시즌 티켓과 같이 여러 이벤트에 대해 단일 패스를 사용할 수도 있습니다.
>




An event ticket can display logo, strip, background, or thumbnail images. However, if you supply a strip image, don’t include a background or thumbnail image. You can also include an extra row of up to four auxiliary fields (for developer guidance, see the `row` property of [PassFields.AuxiliaryFields](https://developer.apple.com/documentation/walletpasses/passfields/auxiliaryfields)).
> 이벤트 티켓은 로고, 스트립, 배경 또는 썸네일 이미지를 표시할 수 있습니다. 그러나 스트립 이미지를 제공하는 경우 배경 또는 축소 이미지를 포함하지 마십시오. 최대 4개의 보조 필드 행을 추가로 포함할 수도 있습니다(개발자 지침은 PassFields의 '행' 속성 참조).보조 필드).
>




• [Example](../technologies/wallet#)
• [Layout](../technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/event-ticket_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/event-ticket_2x.png)


# **Generic passes**

Use the generic style for a type of pass that doesn’t fit into the other categories, such as a gym membership card or coat-check claim ticket. A generic pass can display logo and thumbnail images, and it can have up to four secondary and auxiliary fields, all displayed on one row.
> 체육관 회원 카드 또는 코트 체크 청구권과 같은 다른 범주에 맞지 않는 유형의 패스에 일반적인 스타일을 사용합니다. 일반 패스는 로고 및 섬네일 이미지를 표시할 수 있으며, 최대 4개의 보조 및 보조 필드를 가질 수 있으며, 모두 한 행에 표시됩니다.
>




• [Example](../technologies/wallet#)
• [Layout](../technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/generic_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/generic_2x.png)


# **Passes for Apple Watch**

On Apple Watch, Wallet displays passes in a scrolling carousel of cards. People can add your pass to their Apple Watch even if you don’t create a watch-specific app, so it’s important to understand how your pass can look on the device.
> Apple Watch에서 Wallet은 카드의 회전식 회전대에 패스를 표시합니다. 시계 전용 앱을 만들지 않아도 Apple Watch에 사용자의 패스를 추가할 수 있으므로 단말기에서 사용자의 패스가 어떻게 표시되는지 이해하는 것이 중요합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-pass-design-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-pass-design-intro_2x.png)

On their Apple Watch, people can tap a card to reveal a details screen that displays additional pass information in a scrolling view. In some cases, people can also tap a specific transaction to get more information.
> 애플 워치에서 사람들은 카드를 눌러 스크롤 뷰에 추가 패스 정보를 표시하는 세부 화면을 표시할 수 있다. 경우에 따라, 사람들은 더 많은 정보를 얻기 위해 특정 거래를 탭 할 수도 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-card-and-details_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-card-and-details_2x.png)

Each pass style specifies the fields and images that can appear in the basic layout areas shown below:
> 각 통과 스타일은 아래에 표시된 기본 레이아웃 영역에 나타날 수 있는 필드와 이미지를 지정합니다:
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-layout-diagram_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-layout-diagram_2x.png)

If some information doesn’t fit within the layout areas, the system displays it in the scrolling details screen.
> 일부 정보가 레이아웃 영역에 맞지 않으면 시스템이 스크롤 세부 정보 화면에 표시합니다.
>




**IMPORTANT**In every style, watchOS crops the strip image to fit the aspect ratio of the card interface and may crop white space from other images.
> 모든 스타일에서 중요, 주의OS는 스트립 이미지를 카드 인터페이스의 가로 세로 비율에 맞게 잘라내고 다른 이미지에서 공백을 잘라낼 수 있습니다.
>




• [Boarding](../technologies/wallet#)
• [Coupon](../technologies/wallet#)
• [Store](../technologies/wallet#)
• [Event](../technologies/wallet#)
• [Generic](../technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-layout-boarding-pass_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-layout-boarding-pass_2x.png)


# **Order tracking**

When you support Order Tracking, Wallet can automatically display information about an order after people successfully complete an Apple Pay purchase through your app or website, updating the information whenever the status of the order changes.
> 주문 추적을 지원하는 경우, Wallet은 앱 또는 웹 사이트를 통해 Apple Pay 구매를 성공적으로 완료한 후 주문에 대한 정보를 자동으로 표시하여 주문 상태가 변경될 때마다 정보를 업데이트할 수 있습니다.
>




Wallet presents a dashboard that displays a customer’s active and completed orders. People can choose an order to view details about it, like the items they ordered and fulfillment information for shipping and pickup.
> Wallet은 고객의 활성 주문과 완료된 주문을 표시하는 대시보드를 제공합니다. 주문을 선택하여 주문한 품목과 배송 및 픽업에 대한 배송 정보와 같은 세부 정보를 볼 수 있습니다.
>




The [Wallet Orders](https://developer.apple.com/documentation/walletorders) schema defines the fields you use to provide order data like product descriptions, order status, contact information, and shipping and pickup details, including estimated arrival dates, addresses, tracking numbers, and pickup instructions. Wallet displays the information you supply within consistent, system-defined interfaces. To help people get the information they need quickly and conveniently, supply as much information as you can, using the fields that match your order processes.
> 지갑 주문 스키마는 제품 설명, 주문 상태, 연락처 정보, 예상 도착 날짜, 주소, 추적 번호 및 픽업 지침을 포함한 배송 및 픽업 세부 정보와 같은 주문 데이터를 제공하는 데 사용하는 필드를 정의합니다. 지갑은 일관된 시스템 정의 인터페이스 내에서 사용자가 제공하는 정보를 표시합니다. 사람들이 필요한 정보를 빠르고 편리하게 얻을 수 있도록 주문 프로세스와 일치하는 필드를 사용하여 가능한 한 많은 정보를 제공하십시오.
>




