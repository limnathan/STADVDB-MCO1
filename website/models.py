from . import db

class DimGames(db.Model):
    __tablename__ = 'Dim_games'
    AppID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Release_date = db.Column(db.Date)
    Support_email = db.Column(db.String(100))
    Supported_languages = db.Column(db.Text)
    Audio_languages = db.Column(db.Text)
    Notes = db.Column(db.String(500))

class DimGameAttributes(db.Model):
    __tablename__ = 'Dim_GameAttributes'
    AppID = db.Column(db.Integer, primary_key=True)
    Category = db.Column(db.String(500))
    Tags = db.Column(db.String(1000))
    Genres = db.Column(db.String(1000))

class DimOrganization(db.Model):
    __tablename__ = 'Dim_organization'
    AppID = db.Column(db.Integer, primary_key=True)
    Developers = db.Column(db.String(500))
    Publishers = db.Column(db.String(500))

class DimGamePlatform(db.Model):
    __tablename__ = 'Dim_GamePlatform'
    AppID = db.Column(db.Integer, primary_key=True)
    Windows = db.Column(db.Boolean)
    Mac = db.Column(db.Boolean)
    Linux = db.Column(db.Boolean)

class FactSteamGames(db.Model):
    __tablename__ = 'Fact_steamGames'
    AppID = db.Column(db.Integer, db.ForeignKey('Dim_games.AppID'), db.ForeignKey('Dim_GameAttributes.AppID'), db.ForeignKey('Dim_organization.AppID'), db.ForeignKey('Dim_GamePlatform.AppID'), primary_key=True)
    Estimated_Owners = db.Column(db.Integer)
    Price = db.Column(db.Numeric(10, 2))
    Recommendations = db.Column(db.Integer)
    Metacritic_score = db.Column(db.Integer)
    User_score = db.Column(db.Integer)
    Positive = db.Column(db.Integer)
    Negative = db.Column(db.Integer)
    Score_rank = db.Column(db.Integer)
    Avg_playtime_forever = db.Column(db.Integer)
    Avg_playtime_two_weeks = db.Column(db.Integer)
    Med_playtime_forever = db.Column(db.Integer)
    Med_playtime_two_weeks = db.Column(db.Integer)
    Peak_CCU = db.Column(db.Integer)
    DLC_count = db.Column(db.Integer)
    Discount_DLC = db.Column(db.Integer)
    Achievements = db.Column(db.Integer)

    # Relationships to dimension tables
    game = db.relationship('DimGames', backref='fact_games', lazy=True)
    attributes = db.relationship('DimGameAttributes', backref='fact_attributes', lazy=True)
    organization = db.relationship('DimOrganization', backref='fact_organization', lazy=True)
    platform = db.relationship('DimGamePlatform', backref='fact_platform', lazy=True)

