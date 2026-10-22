from django.contrib import admin
from .models import Document, DocumentChunk


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "status", "size_bytes", "page_count", "uploaded_at")
    list_filter = ("status",)
    search_fields = ("title", "owner__email", "sha256")


@admin.register(DocumentChunk)
class DocumentChunkAdmin(admin.ModelAdmin):
    list_display = ("document", "chunk_index", "page_number")
    exclude = ("embedding",)  # keeps the admin page fast
    raw_id_fields = ("document",)