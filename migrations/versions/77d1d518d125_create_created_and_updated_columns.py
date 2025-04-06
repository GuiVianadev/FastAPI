from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text

# revision identifiers
revision: str = '77d1d518d125'
down_revision: Union[str, None] = 'd2cf1c416383'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Adiciona as colunas como NULLABLE (sem default)
    op.add_column('todos', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('todos', sa.Column('updated_at', sa.DateTime(), nullable=True))

    # Atualiza os registros existentes com CURRENT_TIMESTAMP
    op.execute(text("UPDATE todos SET created_at = CURRENT_TIMESTAMP WHERE created_at IS NULL"))
    op.execute(text("UPDATE todos SET updated_at = CURRENT_TIMESTAMP WHERE updated_at IS NULL"))


def downgrade() -> None:
    op.drop_column('todos', 'updated_at')
    op.drop_column('todos', 'created_at')
