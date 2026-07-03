import random
import time

class Pokemon:
    def __init__(self, nome, tipos, hp, ataque, defesa):
        self.nome = nome
        self.tipos = tipos
        self.hp_max = hp
        self.hp_atual = hp
        self.ataque = ataque
        self.defesa = defesa
        self.golpes = {}

    def aprender_golpe(self, nome_golpe, poder):
        self.golpes[nome_golpe] = poder

    def usar_golpe(self, nome_golpe):
        if nome_golpe in self.golpes:
            poder = self.golpes[nome_golpe]
            # Um cálculo simples de dano baseado no ataque do Pokémon
            dano_base = int((self.ataque * poder) / 50)
            variacao = random.randint(-5, 5) # Um toque de aleatoriedade
            dano_final = max(10, dano_base + variacao)
            
            print(f"🔥 {self.nome} usou {nome_golpe.upper()}!")
            time.sleep(0.5)
            print(f"💥 Causou {dano_final} de dano no oponente!")
            print("-" * 40)
        else:
            print(f"❌ {self.nome} não conhece o golpe {nome_golpe}.")

    def status(self):
        print(f"\n--- Status do {self.nome} ---")
        print(f"Tipo: {' / '.join(self.tipos)}")
        print(f"HP: {self.hp_atual}/{self.hp_max}")
        print(f"Ataque: {self.ataque} | Defesa: {self.defesa}")
        print("Golpes conhecidos:", ", ".join(self.golpes.keys()))
        print("-" * 30)

# --- Criando o seu Charizard ---

# Status base baseados no jogo (com uma leve simplificação)
charizard = Pokemon(
    nome="Charizard", 
    tipos=["Fogo", "Voador"], 
    hp=266, 
    ataque=1009, 
    defesa=105
)

# Ensinando os golpes clássicos
charizard.aprender_golpe("Lança-Chamas (Flamethrower)", poder=90)
charizard.aprender_golpe("Giro Fogo (Fire Spin)", poder=35)
charizard.aprender_golpe("Ataque de Asa (Wing Attack)", poder=600)
charizard.aprender_golpe("Superaquecimento (Overheat)", poder=130)


# --- Executando a demonstração no Terminal ---
if __name__ == "__main__":
    print("¡Um Charizard selvagem apareceu sob o seu comando!")
    charizard.status()
    
    # Simulando alguns ataques
    time.sleep(1)
    charizard.usar_golpe("Giro Fogo (Fire Spin)")
    
    time.sleep(1)
    charizard.usar_golpe("Lança-Chamas (Flamethrower)")
    
    time.sleep(1)
    charizard.usar_golpe("Superaquecimento (Overheat)")