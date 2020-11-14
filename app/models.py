# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
from datetime import datetime, timezone, date
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Sequence,
    Date,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Base:
    __abstract__ = True

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, nullable=True)

    def before_save(self, *args, **kwargs):
        pass

    def after_save(self, *args, **kwargs):
        pass

    def save(self, db, commit=True):
        self.before_save()
        db.add(self)
        if commit:
            try:
                db.commit()
                db.refresh(self)
            except Exception as e:
                db.rollback()
                raise e

        self.after_save()

    @classmethod
    def before_bulk_create(cls, iterable, *args, **kwargs):
        pass

    @classmethod
    def after_bulk_create(cls, model_objs, *args, **kwargs):
        pass

    @classmethod
    def bulk_create(cls, db, iterable, *args, **kwargs):
        cls.before_bulk_create(iterable, *args, **kwargs)
        model_objs = []
        for data in iterable:
            if not isinstance(data, cls):
                data = cls(**data)
            model_objs.append(data)

        cls.bulk_save_objects(db, model_objs)
        if kwargs.get("commit", True) is True:
            db.commit()
        cls.after_bulk_create(model_objs, *args, **kwargs)
        return model_objs

    @classmethod
    def bulk_save_objects(cls, db, model_objs):
        for o in model_objs:
            db.add(o)

    @classmethod
    def bulk_create_or_none(cls, db, iterable, *args, **kwargs):
        try:
            return cls.bulk_create(db, iterable, *args, **kwargs)
        except exc.IntegrityError as e:
            db.rollback()
            return None

    def before_update(self, *args, **kwargs):
        pass

    def after_update(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        self.before_update(*args, **kwargs)
        Base.session.commit()
        self.after_update(*args, **kwargs)

    def delete(self, commit=True):
        Base.session.delete(self)
        if commit:
            Base.session.commit()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


Base = declarative_base(cls=Base)


class Election(Base):
    __tablename__ = "elections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    type = Column(
        String, index=True
    )  # TODO: nrw = Nationalratswahl, ltw = Landtagswahl, grw = gemeinderatswahl, bpw = bundespräsidentenwahl, euw = Europawahl, bmw = bürgermeisterwahl
    shortname = Column(String, nullable=True)
    owat_id = Column(String, unique=True, index=True)
    administrative_level = Column(String, index=True)
    day = Column(Date, nullable=True)
    age_required_active = Column(Integer, nullable=True)
    age_required_passive = Column(Integer, nullable=True)
    wikidata_id = Column(String, unique=True, nullable=True)
    website = Column(String, nullable=True)
    status = Column(String, index=True)  # TODO: define and document possible options
    data_source_organisation = Column(String, nullable=True)
    data_source_link = Column(String, nullable=True)
    data_license = Column(String, nullable=True)
    eligible_voter = Column(Integer, nullable=True)
    total_votes = Column(Integer, nullable=True)
    valid_votes = Column(Integer, nullable=True)
    invalid_votes = Column(Integer, nullable=True)
    vote = relationship("Vote")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.day = date.fromisoformat(kwargs["day"])


class Party(Base):
    __tablename__ = "parties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    shortname = Column(String, nullable=True)
    owat_id = Column(String, unique=True, index=True)
    color = Column(String, nullable=True)
    color_hex = Column(String, nullable=True)
    website = Column(String, nullable=True)
    wikidata_id = Column(String, unique=True, nullable=True)
    eu_family = Column(String, nullable=True)
    vote = relationship("Vote")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NonParty(Base):
    __tablename__ = "nonparties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(
        String, unique=True, index=True
    )  # TODO: define and document possible options
    color = Column(String, nullable=True)
    color_hex = Column(String, nullable=True)
    vote = relationship("Vote")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    gcd_state = Column(String)
    shortname = Column(String, nullable=True)
    owat_id = Column(String, unique=True, index=True, nullable=True)
    wikidata_id = Column(String, unique=True, nullable=True)
    district = relationship("District")
    regionalelectoraldistrict = relationship("RegionalElectoralDistrict")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RegionalElectoralDistrict(Base):
    __tablename__ = "regionalelectoraldistricts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    gcd_regionalelectoraldistrict = Column(String, index=True)
    state_id = Column(Integer, ForeignKey("states.id"))
    wikidata_id = Column(String, unique=True, nullable=True)
    mandates = Column(Integer, nullable=True)
    municipality = relationship("Municipality")


class District(Base):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    state_id = Column(Integer, ForeignKey("states.id"))
    gcd_district = Column(String, unique=True, index=True)
    wikidata_id = Column(String, unique=True, nullable=True)
    municipality = relationship("Municipality")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Municipality(Base):
    __tablename__ = "municipalities"

    id = Column(Integer, primary_key=True, index=True)
    gcd = Column(String, unique=True, index=True)
    gkz = Column(String)
    name = Column(String, index=True)
    district_id = Column(Integer, ForeignKey("districts.id"))
    regionalelectoraldistrict_id = Column(
        Integer, ForeignKey("regionalelectoraldistricts.id"), nullable=True
    )
    wikidata_id = Column(String, unique=True, nullable=True)
    zip_code = Column(String, nullable=True)
    political_status = Column(
        String, nullable=True
    )  # TODO: categories: sr = statutarstadt, st = stadtgemeinde, m = marktgemeinde und blank = Gemeinde ohne Status
    vote = relationship("Vote")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    votes = Column(Integer, nullable=True)
    source = Column(String, nullable=True)
    party_id = Column(Integer, ForeignKey("parties.id"))
    nonparty_id = Column(Integer, ForeignKey("nonparties.id"))
    election_id = Column(Integer, ForeignKey("elections.id"), nullable=False)
    municipality_id = Column(Integer, ForeignKey("municipalities.id"), nullable=False)
