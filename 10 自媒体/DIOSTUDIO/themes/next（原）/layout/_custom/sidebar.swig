<br>
{% if theme.wechat %}
<div class="site-author motion-element" itemprop="author" itemscope itemtype="http://schema.org/Person">
	<img class="site-author-image" itemprop="image" src="{{ url_for( theme.wechat | default(theme.images + '/avatar.gif') ) }}" alt="微信" />
	<p class="site-author-name" itemprop="name">{{ "微信" }}</p>
</div>
{% endif %}

<br>
{% if theme.qq %}
<div class="site-author motion-element" itemprop="author" itemscope itemtype="http://schema.org/Person">
	<img class="site-author-image" itemprop="image" src="{{ url_for( theme.qq | default(theme.images + '/avatar.gif') ) }}" alt="QQ" />
	<p class="site-author-name" itemprop="name">{{ "QQ" }}</p>
</div>
{% endif %}