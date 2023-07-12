---
title: UServerBrowserList
type: class
aliases: UServerBrowserList
share: false

---

# UServerBrowserList





Inherits from UWidget, [IKeyboardFocusInterface](/docs/SDK/Source/Classes/classIKeyboardFocusInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[CreateFakeServers]]**(int32 NumberOfServers, TArray< FString > ServerNames, TArray< FString > MapNamesAndGameModes, TArray< int32 > ListOfPossibleMaxPlayers) |
| void | **[[FetchFilteredList]]**() |
| int32 | **[[GetCurrentFilteredItemsCount]]**() |
| void | **[[GetSelectedSession]]**(FBlueprintSessionResult & Out) |
| UWidget * | **[[GetSelectedWidget]]**() |
| void | **[[OnPingServerComplete]]**(FBlueprintSessionResult PingedSession) |
| void | **[[OnQueryCompleted]]**(bool bSuccess, EServerListType ListType) |
| void | **[[OnRefreshCompleted]]**(bool bSuccess, EServerListType ListType) |
| void | **[[RefreshServerEntry]]**(FBlueprintSessionResult SessionResult) |
| void | **[[RefreshServerList]]**(EServerListType ListType) |
| void | **[[SelectFirstWidget]]**() |
| void | **[[SelectWidget]]**(const FBlueprintSessionResult & Item) |
| void | **[[SortServersByGameMode]]**(bool Descending) |
| void | **[[SortServersByMapName]]**(bool Descending) |
| void | **[[SortServersByPing]]**(bool Descending) |
| void | **[[SortServersByPlayerNumbers]]**(bool Descending) |
| void | **[[SortServersByServerName]]**(bool Descending) |
| void | **[[SortServersByServerType]]**(bool Descending) |
| | **[[UServerBrowserList]]**() |
| void | **[[UseSavedSort]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[ItemHeight]]**  |
| FOnGenerateRowSessionResult | **[[OnGenerateRowEvent]]**  |
| FOnGetServerFilterSettings | **[[OnGetServerFilterSettingsEvent]]**  |
| FOnLoadingProgressStatusChanged | **[[OnLoadingProgressStatusChangedEvent]]**  |
| FOnRefreshServerComplete | **[[OnRefreshServerCompleteEvent]]**  |
| FOnSelectionChanged | **[[OnSelectionChangedEvent]]**  |
| TEnumAsByte< ESelectionMode::Type > | **[[SelectionMode]]**  |
| FName | **[[TableRowStyleName]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [UTBLScrollBarStyleDataAsset](/docs/SDK/Source/Classes/classUTBLScrollBarStyleDataAsset.md) * | **[[ScrollBarStyle]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200