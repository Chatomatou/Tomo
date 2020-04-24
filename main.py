#coding: utf-8
import common.GameManager as common
import sys 

def main():
    manager = common.GameManager("Titre de la fenêtre", 800, 600, 60)
    
    if not manager.initialize():
        print("Impossible d'initializer le manager de jeux...")
        return -1
    
    manager.run()
    return 0

if __name__ == "__main__":
    sys.exit(main())