---
title: UFriendsAndPartyList
type: class
aliases: UFriendsAndPartyList
share: false

---

# UFriendsAndPartyList





Inherits from UListViewBase

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[BP_NavigateToItem]]**(const [FBlueprintOnlineUser](/docs/SDK/Source/Classes/structFBlueprintOnlineUser.md) & Item) |
| void | **[[RefreshFriendsList]]**(bool ShouldRead) |
| void | **[[RefreshItemsList]]**() |
| void | **[[SetPartyInviteSettings]]**(bool bAllowInvites, bool bJoinViaPresence, bool bJoinViaPresenceFriendsOnly) |
| | **[[UFriendsAndPartyList]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FOnListEntryGeneratedDynamicWithSelf | **[[BP_OnEntryGeneratedWithSelf]]**  |
| FOnListEntryRefreshed | **[[BP_OnListEntryRefreshed]]**  |
| EFriendsListType | **[[ListType]]**  |
| FOnGetEntryWidgetClassForItem | **[[OnGetEntryWidgetClassForItemEvent]]**  |
| [UTBLScrollBarStyleDataAsset](/docs/SDK/Source/Classes/classUTBLScrollBarStyleDataAsset.md) * | **[[ScrollBarStyle]]**  |
| TMap< EFriendsListType, int32 > | **[[SortingWeights]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| EConsumeMouseWheel | **[[ConsumeMouseWheel]]**  |
| float | **[[EntrySpacing]]**  |
| TEnumAsByte< EOrientation > | **[[Orientation]]**  |
| TEnumAsByte< ESelectionMode::Type > | **[[SelectionMode]]**  |
| bool | **[[bClearSelectionOnClick]]**  |
| bool | **[[bIsFocusable]]**  |
| bool | **[[bReturnFocusToSelection]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200