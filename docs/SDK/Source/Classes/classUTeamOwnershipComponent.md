---
title: UTeamOwnershipComponent
type: class
aliases: UTeamOwnershipComponent
share: false

---

# UTeamOwnershipComponent





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| EFaction | **[[GetFaction]]**() const |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| [ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * | **[[GetOwnerTeam]]**() |
| void | **[[OnRep_OwnerFaction]]**() |
| void | **[[SetFaction]]**(EFaction Faction) |
| void | **[[SetOwnerFaction]]**(EFaction Faction) |
| void | **[[SetOwnerTeam]]**([ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * Team) |
| | **[[UTeamOwnershipComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| EFaction | **[[DefaultFaction]]**  |
| FOwnershipSignature | **[[OnOwnershipChanged]]**  |
| [FReplicated_EFaction](/docs/SDK/Source/Classes/structFReplicated__EFaction.md) | **[[OwnerFaction]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200