#include <list>
#include <string>
#include <iostream>

#pragma once

enum class PublicationType { Newspaper, Magazine };

using Publication = std::tuple<PublicationType, std::string, double>;

std::istream& operator>>(std::istream& is, PublicationType& type);
std::ostream& operator<<(std::ostream& out, PublicationType type);
std::ostream& operator<<(std::ostream& out, const std::list<Publication>& pubs);
void addPublication(std::list<Publication>& pubs, const Publication& pub);
bool loadPublications(std::list<Publication>& pubs, const std::string& filename);
bool savePublications(const std::list<Publication>& pubs, const std::string& filename);
