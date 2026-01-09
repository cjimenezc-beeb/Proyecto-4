classDiagram
    %% Definición de la Clase Abstracta Padre
    class Cliente {
        <<Abstract>>
        -String __dni
        +String nombre
        +String email
        +Cliente(dni, nombre, email)
        +get_dni()
        +mostrar_beneficio()*
    }

    %% Definición de las Clases Hijas
    class ClienteRegular {
        +mostrar_beneficio()
    }

    class ClientePremium {
        +mostrar_beneficio()
    }

    class ClienteCorporativo {
        +mostrar_beneficio()
    }

    %% Relaciones de Herencia (La flecha apunta al padre)
    Cliente <|-- ClienteRegular
    Cliente <|-- ClientePremium
    Cliente <|-- ClienteCorporativo