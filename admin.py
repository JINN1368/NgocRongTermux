�
    R�Kf|(  �                   ��   � d dl Z d dlZd dlZdZdZdZdZdZdZ	e� de� d	e� d
�Z
e� de� de� d
�Ze� de� de� d
�Ze� de� de� d
�Ze	� de� de	� d
�Zd� Zd� Zd� Z e�   �          dS )�    Nz[0;91mz[0;37mz[0;92mz[0;93mz[0;34mz[0;36m�[�OK�]�EXC�i�!u   NHẬP LỰA CHỌNc                  �.   � t          j        d�  �         d S )N�clear)�
subprocess�run� �    �admin.py�Clrscrr      s   � ��N�7�����r   c                  �.   � t          j        d�  �         d S )Nzsleep 3)�os�systemr   r   r   �Pauser      s   � ��I�i�����r   c                  �   � t          �   �          t          j        �                    dddd��  �        } | �                    �   �         }d}|�                    |�  �         |D ]0\  }}t          t          � dt          � |� t          � d|� d	��  �         �1t          t          t          � d
��  �        �  �        }t          �   �          d}|�                    ||f�  �         |�                    �   �         d         }t          |�  �        }t          t          � dt          � dt          � dt          � d|d         � d|d         � dt          � d��  �         t          t          � dt          � dt          � dt          � d|d         � d|d         � dt          � d��  �         t          t          � dt          � dt          � dt          � d|d         � dt          � d��  �         t          t          � dt          � dt          � dt          � d|d         � dt          � d��  �         t          t          � dt          � dt          � dt          � d|d          � dt          � d��  �         d!}|�                    ||f�  �         |�                    �   �         d         }t          |�  �        }g d"�}t          t          � dt          � d#t          � d$t          � ||d                  � dt          � d��  �         d%}|�                    ||f�  �         |�                    �   �         d         }t          |�  �        }t          t          � dt          � d&t          � d't          � |d         � t          � d�
�  �         t          t          � dt          � d(t          � d)t          � |d         � dt          � d��  �         t          t          � dt          � d*t          � d+t          � |d         � dt          � d��  �         d,}|�                    ||f�  �         |�                    �   �         d         }|dk    r8t          t          � dt          � d-t          � d.t          � d/t          � d�
�  �         n7t          t          � dt          � d-t          � d.t          � d0t          � d�
�  �         t          d1�  �         t          t          � d2t          � d3t          � d4��  �         t          d1�  �         t          t          � �  �        }	 |dk    r�d}|�                    ||f�  �         |�                    �   �         d         }t          |�  �        }t          t          d6�  �        �  �        }	|	|d<   |	|d<   d7}
|�                    |
t!          |�  �        |f�  �         | �                    �   �          t%          �   �          �ns|dk    r�d}|�                    ||f�  �         |�                    �   �         d         }t          |�  �        }t          t          d8�  �        �  �        }	|	|d<   |	|d<   d7}
|�                    |
t!          |�  �        |f�  �         | �                    �   �          t%          �   �          �n�|dk    r�d}|�                    ||f�  �         |�                    �   �         d         }t          |�  �        }t          t          d9�  �        �  �        }	|	|d<   d7}
|�                    |
t!          |�  �        |f�  �         | �                    �   �          t%          �   �          �n|dk    r�d}|�                    ||f�  �         |�                    �   �         d         }t          |�  �        }t          t          d:�  �        �  �        }	|	|d<   d7}
|�                    |
t!          |�  �        |f�  �         | �                    �   �          t%          �   �          �nR|dk    r�d}|�                    ||f�  �         |�                    �   �         d         }t          |�  �        }t          t          d;�  �        �  �        }	|	|d <   d7}
|�                    |
t!          |�  �        |f�  �         | �                    �   �          t%          �   �          �n�|d#k    r�d!}|�                    ||f�  �         |�                    �   �         d         }t          |�  �        }t          t          d<�  �        �  �        }	|	|d<   d|d<   d|d<   d=}
|�                    |
t!          |�  �        |f�  �         | �                    �   �          t%          �   �          �n�|d&k    r�d%}|�                    ||f�  �         |�                    �   �         d         }t          |�  �        }t          t          d>�  �        �  �        }	|	|d<   d?}
|�                    |
t!          |�  �        |f�  �         | �                    �   �          t%          �   �          �n,|d(k    r�d%}|�                    ||f�  �         |�                    �   �         d         }t          |�  �        }t          t          d@�  �        �  �        }	|	|d<   d?}
|�                    |
t!          |�  �        |f�  �         | �                    �   �          t%          �   �          �nx|d*k    r�d%}|�                    ||f�  �         |�                    �   �         d         }t          |�  �        }t          t          dA�  �        �  �        }	|	|d<   d?}
|�                    |
t!          |�  �        |f�  �         | �                    �   �          t%          �   �          n�|d-k    r�d,}|�                    ||f�  �         |�                    �   �         d         }t          t          dB�  �        �  �        }	|	}dC}
|�                    |
t!          |�  �        |f�  �         | �                    �   �          t%          �   �          n$t'          j        dDdEg�  �         t+          �   �          ��.)FN�	localhost�root� �JINN_FREE_V2)�host�user�password�databasez#SELECT account_id, name FROM playerr   z]: z* 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~u   NHẬP ID TÀI KHOẢN z3SELECT data_point FROM player WHERE account_id = %sr   �1z
] TN, SM [� �   z, �   r   �2u   ] MÁU, KI [�   �   �3u   ] SỨC ĐÁNH[�   �4u   ] GIÁP[�   �5u   ] CHÍ MẠNG[�	   z2SELECT data_task FROM player WHERE account_id = %s)!u   Nhiệm vụ đầu tiênu   Nhiệm vụ tập luyệnu   Nhiệm vụ tìm thức ănu   Tìm kiếm sao băngu   Nhiệm vụ khó khănu#   Nhiệm vụ gia tăng sức mạnhu   Nhiệm vụ trò chuyệnu   Nhiệm vụ giải cứuu#   Nhiệm vụ ân nhân xuất sắcu   Nhiệm vụ tiên học lễu   Nhiệm vụ học phíu   Nhiệm vụ kết giaou   Nhiệm vụ xin phépu"   Nhiệm vụ gia nhập bang hộiu   Nhiệm vụ bang hội lần 1u   Nhiệm vụ bang hội lần 2u   Tiêu diệt quái vậtu   Nhiệm vụ giúp đỡ Cuiu   Nhiệm vụ bất khả thiu$   Nhiệm vụ chạm trán đệ tửu%   Nhiệm vụ Tiểu Đội Sát Thủu(   Nhiệm vụ chạm trán Fide đại cau5   Nhiệm vụ chạm trán Rôbốt sát thủ lần 1u5   Nhiệm vụ chạm trán Rôbốt sát thủ lần 2u-   Nhiệm vụ giải cứu thị trấn Ginder�   Tiêu Diệt Xên Đi Mấy Emr+   u   Kết Bạn Nhìu Niềm Vuiu   Săn Xên Bên Võ Đài Nhéu   Qua Cold Nhéu#   Pem Chết Cụ Tụi Doraemon Đi u   Nhiệm Vụ Hơi Khóu$   Đã Hoàn Thành Hết Nhiệm Vụ�6u   ] NHIỆM VỤ [ z7SELECT data_inventory FROM player WHERE account_id = %s�7u
   ] VÀNG [ �8u   ] NGỌC [ �9u   ] HỒNG NGỌC [ z*SELECT is_admin FROM account WHERE id = %s�10u   ] QUYỀN ADMIN [ u    CÓ u    KHÔNG z,-- -- -- -- -- -- -- -- -- -- -- -- -- -- --u0    HÃY XEM KĨ VIDEO HƯỚNG DẪN TRÊN YOTUBE
u$    NHẤN ENTER ĐỂ QUAY LẠI MENU
u1    BUFF QUÁ NHIỀU SẼ KHÔNG VÀO ĐƯỢC GAMETu   NHẬP SỨC MẠNH: z7UPDATE player SET data_point = %s WHERE account_id = %su   NHẬP HP, KI: u   NHẬP SỨC ĐÁNH: u   NHẬP GIÁP: u   NHẬP CHÍ MẠNG(MAX:100): u   NHẬP ID NHIỆM VỤ(1-32): z6UPDATE player SET data_task = %s WHERE account_id = %su   NHẬP VÀNG: z;UPDATE player SET data_inventory = %s WHERE account_id = %su   NHẬP NGỌC: u   NHẬP HỒNG NGỌC: u   NHẬP(1: có, 0: không): z.UPDATE account SET is_admin = %s WHERE id = %s�pythonzmain.py)r   �mysql�	connector�connect�cursor�execute�print�BLUE�WHITE�int�input�THONGTIN�fetchone�eval�CANHBAO�NHAP�str�commit�mainr   �call�exit)�connr5   �select_query�id�	col_value�row_id�	col_array�task�choose�	new_value�update_querys              r   rC   rC      s�  � �
�H�H�H��?�"�"���� �	 #� � �D� �[�[�]�]�F�8�L�
�N�N�<� � � � "� d� d���Y���b�b��b�r�b�4�b�b�I�b�b�b�c�c�c�c���(�;�;�;�<�<�=�=�F�
�H�H�H�H�L�
�N�N�<�&��+�+�+����!�!�!�$�I��Y���I�	�t�
^�
^�e�
^�
^�d�
^�
^�e�
^�
^�i��l�
^�
^�i�PQ�l�
^�
^�UY�
^�
^�
^�_�_�_�	�t�
`�
`�e�
`�
`�d�
`�
`��
`�
`�	�!��
`�
`�	�RS��
`�
`�W[�
`�
`�
`�a�a�a�	�t�
S�
S�e�
S�
S�d�
S�
S�5�
S�
S�9�Q�<�
S�
S�$�
S�
S�
S�T�T�T�	�t�
L�
L�e�
L�
L�d�
L�
L�E�
L�
L�I�a�L�
L�
L�4�
L�
L�
L�M�M�M�	�t�
R�
R�e�
R�
R�d�
R�
R�%�
R�
R�)�A�,�
R�
R��
R�
R�
R�S�S�S�G�L�
�N�N�<�&��+�+�+����!�!�!�$�I��Y���I� q�  q�  q�D�	�t�
Z�
Z�e�
Z�
Z�d�
Z�
Z�U�
Z�D��1��<N�
Z�
Z�QU�
Z�
Z�
Z�[�[�[�L�L�
�N�N�<�&��+�+�+����!�!�!�$�I��Y���I�	�t�
L�
L�e�
L�
L�d�
L�
L�e�
L�Y�q�\�
L�4�
L�
L�
L�M�M�M�	�t�
N�
N�e�
N�
N�d�
N�
N�u�
N�i��l�
N�
N�T�
N�
N�
N�O�O�O�	�t�
U�
U�e�
U�
U�d�
U�
U�e�
U�Y�q�\�
U�
U�D�
U�
U�
U�V�V�V�?�L�
�N�N�<�&��+�+�+����!�!�!�$�I��A�~�~��4�P�P�%�P�P�4�P�P�5�P�P�t�P�P�P�Q�Q�Q�Q��4�S�S�%�S�S�4�S�S�5�S�S�$�S�S�S�T�T�T�	�
8�9�9�9�	�w�  t�  t��  t�  t�w~�  t�  t�  t�  u�  u�  u�	�
8�9�9�9���=�!�!�F�t��S�=�=�P�L��N�N�<�&��3�3�3����)�)�!�,�I��Y���I��E�"9�:�:�;�;�I�$�I�a�L�$�I�a�L�T�L��N�N�<�#�i�.�.�&�)A�B�B�B��K�K�M�M�M��F�F�F�F��s�]�]�P�L��N�N�<�&��3�3�3����)�)�!�,�I��Y���I��E�"3�4�4�5�5�I�$�I�a�L�$�I�a�L�T�L��N�N�<�#�i�.�.�&�)A�B�B�B��K�K�M�M�M��F�F�F�F��s�]�]�P�L��N�N�<�&��3�3�3����)�)�!�,�I��Y���I��E�"9�:�:�;�;�I�$�I�a�L�T�L��N�N�<�#�i�.�.�&�)A�B�B�B��K�K�M�M�M��F�F�F�F��s�]�]�P�L��N�N�<�&��3�3�3����)�)�!�,�I��Y���I��E�"2�3�3�4�4�I�$�I�a�L�T�L��N�N�<�#�i�.�.�&�)A�B�B�B��K�K�M�M�M��F�F�F�F��s�]�]�P�L��N�N�<�&��3�3�3����)�)�!�,�I��Y���I��E�"A�B�B�C�C�I�$�I�a�L�T�L��N�N�<�#�i�.�.�&�)A�B�B�B��K�K�M�M�M��F�F�F�F��s�]�]�O�L��N�N�<�&��3�3�3����)�)�!�,�I��Y���I��E�"B�C�C�D�D�I�$�I�a�L��I�a�L��I�a�L�S�L��N�N�<�#�i�.�.�&�)A�B�B�B��K�K�M�M�M��F�F�F�F��s�]�]�T�L��N�N�<�&��3�3�3����)�)�!�,�I��Y���I��E�"2�3�3�4�4�I�$�I�a�L�X�L��N�N�<�#�i�.�.�&�)A�B�B�B��K�K�M�M�M��F�F�F�F��s�]�]�T�L��N�N�<�&��3�3�3����)�)�!�,�I��Y���I��E�"3�4�4�5�5�I�$�I�a�L�X�L��N�N�<�#�i�.�.�&�)A�B�B�B��K�K�M�M�M��F�F�F�F��s�]�]�T�L��N�N�<�&��3�3�3����)�)�!�,�I��Y���I��E�":�;�;�<�<�I�$�I�a�L�X�L��N�N�<�#�i�.�.�&�)A�B�B�B��K�K�M�M�M��F�F�F�F��t�^�^�G�L��N�N�<�&��3�3�3����)�)�!�,�I��E�"?�@�@�A�A�I�!�I�K�L��N�N�<�#�i�.�.�&�)A�B�B�B��K�K�M�M�M��F�F�F�F��O�X�i�0�1�1�1��F�F�F�itr   )r   r   �mysql.connectorr2   �REDr9   �GREEN�YELLOWr8   �CYAN�XONG�DANGTHUCTHIr<   r?   r@   r   r   rC   r   r   r   �<module>rW      s#  �� &� &� &� &� &� &� &� &� &� &� &� &� ������������ �'�'�E�'�'�U�'�'�'���1�1�E�1�1�f�1�1�1���(�(�u�(�(�t�(�(�(���
%�
%�U�
%�
%�S�
%�
%�
%���6�6�5�6�6�T�6�6�6��� � �� � �m� m� m�\ ������r   