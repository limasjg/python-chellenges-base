```mermaid
graph TD
    subgraph "Internet"
        User[👤 Usuário Final]
    end

    subgraph "AWS Cloud"
        subgraph "Região AWS"
            Route53[🌐 Route 53] --> ALB

            subgraph "VPC"
                IGW[🚪 Internet Gateway]
                subgraph "Sub-rede Pública A (AZ 1)"
                    ALB[⚖️ Application Load Balancer]
                    NAT_A[🌐 NAT Gateway A]
                end
                subgraph "Sub-rede Pública B (AZ 2)"
                    ALB_replica[⚖️ Application Load Balancer]
                end

                ALB --> ASG
                ALB_replica --> ASG

                subgraph "Sub-rede Privada A (AZ 1)"
                    ECS_A[💻 ECS Task / EC2]
                    RDS_A[📦 RDS Primary (PostgreSQL/MySQL)]
                end

                subgraph "Sub-rede Privada B (AZ 2)"
                    ECS_B[💻 ECS Task / EC2]
                    RDS_B[📦 RDS Read Replica]
                end

                ECS_A --> S3
                ECS_B --> S3
                ECS_A --> RDS_A
                ECS_B --> RDS_A

                subgraph "Recursos Globais/VPC"
                    ASG[🔄 Auto Scaling Group]
                    S3[🗄️ S3 Bucket<br><i>(Armazenamento de Imagens)</i>]
                    CW[📊 CloudWatch<br><i>(Logs, Métricas, Alarmes)</i>]
                    IAM[🔑 IAM Roles & Policies]
                end
            end
        end
    end

    User --> Route53
    Route53 -- "DNS Query" --> ALB
    ALB -- "Encaminha tráfego" --> ECS_A & ECS_B

    ECS_A -- "Acesso à Internet" --> NAT_A
    ECS_B -- "Acesso à Internet" --> NAT_A
    NAT_A --> IGW

    ECS_A & ECS_B -- "Leitura/Escrita de Dados" --> RDS_A
    ECS_A & ECS_B -- "Leitura de Dados" --> RDS_B
    RDS_A -- "Replicação" --> RDS_B

    ECS_A & ECS_B -- "Upload/Download de Imagens" --> S3

    ECS_A & ECS_B -- "Envia Métricas/Logs" --> CW
    RDS_A & RDS_B -- "Envia Métricas/Logs" --> CW
    ALB -- "Envia Métricas/Logs" --> CW
    CW -- "Aciona Alarme" --> ASG
    ASG -- "Escala" --> ECS_A & ECS_B

    style User fill:#cde4ff
    style Route53 fill:#ffc8dd
    style ALB fill:#ffc8dd
    style ALB_replica fill:#ffc8dd
    style ECS_A fill:#a2d2ff
    style ECS_B fill:#a2d2ff
    style RDS_A fill:#bde0fe
    style RDS_B fill:#bde0fe
    style S3 fill:#f1c0e8
    style CW fill:#f1c0e8
    style IAM fill:#f1c0e8
    style ASG fill:#f1c0e8
