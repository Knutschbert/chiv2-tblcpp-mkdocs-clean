---
title: UObjectiveStatusDisplayComponent
type: class
aliases: UObjectiveStatusDisplayComponent
share: false

---

# UObjectiveStatusDisplayComponent





Inherits from [UDisplayComponent](/docs/SDK/Source/Classes/classUDisplayComponent.md), [IPlayerInHudMarkerZoneInterface](/docs/SDK/Source/Classes/classIPlayerInHudMarkerZoneInterface.md), UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), [IDisplayComponentInterface](/docs/SDK/Source/Classes/classIDisplayComponentInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual bool | **[[IsLocalPlayerInHudMarkerZone]]**() override |
| | **[[UObjectiveStatusDisplayComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| UMaterialInstance * | **[[ActiveObjectiveIcon]]**  |
| UMaterialInstance * | **[[ContestedObjectiveIcon]]**  |
| FText | **[[DefaultAgathaText]]**  |
| FText | **[[DefaultMasonText]]**  |
| EObjectiveState | **[[DefaultObjectiveState]]**  |
| EFaction | **[[DefaultOwningTeam]]**  |
| float | **[[DefaultProgress]]**  |
| FText | **[[DefaultTenosiaText]]**  |
| bool | **[[ShowProgress]]**  |
| bool | **[[bLocalPlayerInsideZone]]**  |
| bool return | **[[false]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200