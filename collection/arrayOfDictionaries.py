EnglishTelugu = {'cat':'pilli','dog':'kukka','man':'mogadu'}
EnglishTamil = {'cat':'poonai', 'dog':'naay','man':'manithan'}
EnglishHindi = {'cat': 'billi','dog':'kutta','man':'mard'}

arrayOfNouns = [EnglishTelugu,EnglishTamil, EnglishHindi]

for x in arrayOfNouns:
    print(x['cat'], x['dog'])