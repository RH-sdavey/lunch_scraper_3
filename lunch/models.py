"""What every restaurant parser produces: plain, structured data (no HTML)."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date


@dataclass
class Dish:
    name: str
    kind: str = "main"            # "soup" | "main"
    price: int | None = None      # Kč


@dataclass
class DayMenu:
    day: date
    dishes: list[Dish] = field(default_factory=list)
    note: str | None = None       # e.g. "Státní svátek – výběr z jídelního lístku"


@dataclass
class Menu:
    restaurant: str               # registry id
    days: list[DayMenu] = field(default_factory=list)
    error: str | None = None

    def for_day(self, d: date) -> DayMenu | None:
        return next((x for x in self.days if x.day == d), None)

    def to_dict(self) -> dict:
        out = asdict(self)
        for x in out["days"]:
            x["day"] = x["day"].isoformat()
        return out

    @classmethod
    def from_dict(cls, d: dict) -> "Menu":
        days = [DayMenu(day=date.fromisoformat(x["day"]), note=x.get("note"),
                        dishes=[Dish(**dish) for dish in x["dishes"]]) for x in d.get("days", [])]
        return cls(restaurant=d["restaurant"], days=days, error=d.get("error"))
