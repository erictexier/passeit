/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_parse_format.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/12/02 18:52:23 by etexier           #+#    #+#             */
/*   Updated: 2019/12/02 19:32:48 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int			pf_parse_format(const char *str, va_list list)
{
	size_t			i;
	size_t			start;
	int				valid;
	int				count;

	i = 0;
	count = 0;
	while (str[i])
	{
		start = i;
		valid = 0;
		if (str[i] == '%')
		{
			i++;
			if (parse_one(str, &i, &valid))
				continue;
		}
		else
			while (str[i] && str[i] != '%')
				i++;
		count += get_next(str + start, i - start, valid, list);
	}
	return (count);
}