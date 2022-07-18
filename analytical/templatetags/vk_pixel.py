import re

from django.template import Library, Node

from analytical.utils import get_required_setting, is_internal_ip, disable_html

VK_PIXEL_HEAD_CODE = """\
<script type="text/javascript">
!function(){var t=document.createElement("script");t.type="text/javascript",t.async=!0,t.src='https://vk.com/js/api/openapi.js?169',t.onload=function(){VK.Retargeting.Init('%(VK_PIXEL_ID)s'),VK.Retargeting.Hit()},document.head.appendChild(t)}();
</script>
<noscript>
<img src='https://vk.com/rtrg?p=%(VK_PIXEL_ID)s' style="position:fixed; left:-999px;" alt=""/>
</noscript>
"""

register = Library()


@register.tag
def vk_pixel_head(parser, token):
    """
    VK Pixel head temlate tag
    """
    return VKPixelHeadNode()


class VKPixelHeadNode(Node):
    def __init__(self):
        self.pixel_id = get_required_setting(
            'VK_PIXEL_ID',
            re.compile(r'^VK'),
            "must be (a string containing) a number",
        )

    def render(self, context):
        html = VK_PIXEL_HEAD_CODE % {'VK_PIXEL_ID': self.pixel_id}
        if is_internal_ip(context, 'VK_PIXEL'):
            return disable_html(html, 'VK Pixel')
        else:
            return html


def contribute_to_analytical(add_node):
    VKPixelHeadNode()
    add_node("head_bottom", VKPixelHeadNode)
